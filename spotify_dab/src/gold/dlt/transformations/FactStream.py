import dlt

@dlt.table
def factstream_stg():
  df = spark.readStream.table("spotify_databricks.silver.factstream")
  return df

dlt.create_streaming_table("factstream")

dlt.create_auto_cdc_flow(
    target = "factstream",
    source = "factstream_stg",
    keys = ["stream_id"],
    sequence_by = "date_key",
    stored_as_scd_type = 1
)
