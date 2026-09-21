import dlt

@dlt.table
def dimuser_stg():
  df = spark.readStream.table("spotify_databricks.silver.dim_user")
  return df

dlt.create_streaming_table("dimuser")

dlt.create_auto_cdc_flow(
    target = "dimuser",
    source = "dimuser_stg",
    keys = ["user_id"],
    sequence_by = "updated_at",
    stored_as_scd_type = 2
)
