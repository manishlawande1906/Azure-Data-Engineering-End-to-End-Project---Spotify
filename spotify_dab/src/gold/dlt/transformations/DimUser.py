import dlt

@dlt.table
def dimartist_stg():
  df = spark.readStream.table("spotify_databricks.silver.dimartist")
  return df

dlt.create_streaming_table("dimartist")

dlt.create_auto_cdc_flow(
    target = "dimartist",
    source = "dimartist_stg",
    keys = ["artist_id"],
    sequence_by = "updated_at",
    stored_as_scd_type = 2
)
