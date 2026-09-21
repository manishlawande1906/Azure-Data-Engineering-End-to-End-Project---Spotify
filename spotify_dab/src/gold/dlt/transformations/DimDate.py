import dlt

@dlt.table
def dimdate_stg():
  df = spark.readStream.table("spotify_databricks.silver.dimdate")
  return df

dlt.create_streaming_table("dimdate")

dlt.create_auto_cdc_flow(
    target = "dimdate",
    source = "dimdate_stg",
    keys = ["date_key"],
    sequence_by = "date",
    stored_as_scd_type = 2
)
