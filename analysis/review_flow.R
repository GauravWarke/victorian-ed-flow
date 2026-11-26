# Run from the repository root with Rscript analysis/review_flow.R
records <- read.csv("data/annual-results.csv", check.names = FALSE,
                    fileEncoding = "UTF-8")
required <- c("Financial year", "Metric", "Result (%)", "Target (%)",
              "Shortfall (percentage points)")
stopifnot(all(required %in% names(records)))
flow <- records[required]
names(flow) <- c("year", "measure", "actual", "target", "published_gap")
stopifnot(!anyNA(flow), !anyDuplicated(flow[c("year", "measure")]))
flow$gap <- round(flow$target - flow$actual, 1)
stopifnot(all(abs(flow$gap - flow$published_gap) <= 0.05))
latest <- subset(flow, year == max(year))
latest <- latest[order(-latest$gap), ]
print(latest[c("year", "measure", "actual", "target", "gap")], row.names = FALSE)
cat(sprintf("\n%d of %d standards met target.\n",
            sum(latest$actual >= latest$target), nrow(latest)))
for (measure in unique(flow$measure)) {
  series <- flow[flow$measure == measure, ]
  if (nrow(series) < 2) next
  series <- series[order(series$year), ]
  change <- tail(series$actual, 1) - series$actual[1]
  cat(sprintf("%s (%s to %s): %+.1f percentage points\n",
              measure, series$year[1], tail(series$year, 1), change))
}
