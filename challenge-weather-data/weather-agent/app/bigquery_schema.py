# bq show --format=prettyjson bigquery-public-date:noaa_gsod.gsod2025
GSOD_DS_SCHEMA = """
{
  "creationTime": "1736412756859",
  "description": "",
  "etag": "WIW2r9rpByAdAaEcY+WU1w==",
  "id": "bigquery-public-data:noaa_gsod.gsod2025",
  "kind": "bigquery#table",
  "lastModifiedTime": "1763320037960",
  "location": "US",
  "numActiveLogicalBytes": "492127170",
  "numActivePhysicalBytes": "40404868",
  "numBytes": "492127170",
  "numCurrentPhysicalBytes": "40404868",
  "numLongTermBytes": "0",
  "numLongTermLogicalBytes": "0",
  "numLongTermPhysicalBytes": "0",
  "numRows": "2528312",
  "numTimeTravelPhysicalBytes": "0",
  "numTotalLogicalBytes": "492127170",
  "numTotalPhysicalBytes": "40404868",
  "schema": {
    "fields": [
      {
        "description": "Cloud - GSOD NOAA",
        "mode": "NULLABLE",
        "name": "stn",
        "type": "STRING"
      },
      {
        "description": "WBAN number where applicable--this is the historical \"Weather Bureau Air Force Navy\" number - with WBAN being the acronym",
        "mode": "NULLABLE",
        "name": "wban",
        "type": "STRING"
      },
      {
        "description": "Date of the weather observations",
        "mode": "NULLABLE",
        "name": "date",
        "type": "DATE"
      },
      {
        "description": "The year",
        "mode": "NULLABLE",
        "name": "year",
        "type": "STRING"
      },
      {
        "description": "The month",
        "mode": "NULLABLE",
        "name": "mo",
        "type": "STRING"
      },
      {
        "description": "The day",
        "mode": "NULLABLE",
        "name": "da",
        "type": "STRING"
      },
      {
        "description": "Mean temperature for the day in degrees Fahrenheit to tenths. Missing = 9999.9",
        "mode": "NULLABLE",
        "name": "temp",
        "type": "FLOAT"
      },
      {
        "description": "Number of observations used in calculating mean temperature",
        "mode": "NULLABLE",
        "name": "count_temp",
        "type": "INTEGER"
      },
      {
        "description": "Mean dew point for the day in degreesm Fahrenheit to tenths.  Missing = 9999.9",
        "mode": "NULLABLE",
        "name": "dewp",
        "type": "FLOAT"
      },
      {
        "description": "Number of observations used in calculating mean dew point",
        "mode": "NULLABLE",
        "name": "count_dewp",
        "type": "INTEGER"
      },
      {
        "description": "Mean sea level pressure for the day in millibars to tenths. Missing = 9999.9",
        "mode": "NULLABLE",
        "name": "slp",
        "type": "FLOAT"
      },
      {
        "description": "Number of observations used in calculating mean sea level pressure",
        "mode": "NULLABLE",
        "name": "count_slp",
        "type": "INTEGER"
      },
      {
        "description": "Mean station pressure for the day in millibars to tenths. Missing = 9999.9",
        "mode": "NULLABLE",
        "name": "stp",
        "type": "FLOAT"
      },
      {
        "description": "Number of observations used in calculating mean station pressure",
        "mode": "NULLABLE",
        "name": "count_stp",
        "type": "INTEGER"
      },
      {
        "description": "Mean visibility for the day in miles to tenths.  Missing = 999.9",
        "mode": "NULLABLE",
        "name": "visib",
        "type": "FLOAT"
      },
      {
        "description": "Number of observations used in calculating mean visibility",
        "mode": "NULLABLE",
        "name": "count_visib",
        "type": "INTEGER"
      },
      {
        "description": "Mean wind speed for the day in knots to tenths. Missing = 999.9",
        "mode": "NULLABLE",
        "name": "wdsp",
        "type": "STRING"
      },
      {
        "description": "Number of observations used in calculating mean wind speed",
        "mode": "NULLABLE",
        "name": "count_wdsp",
        "type": "STRING"
      },
      {
        "description": "Maximum sustained wind speed reported for the day in knots to tenths. Missing = 999.9",
        "mode": "NULLABLE",
        "name": "mxpsd",
        "type": "STRING"
      },
      {
        "description": "Maximum wind gust reported for the day in knots to tenths. Missing = 999.9",
        "mode": "NULLABLE",
        "name": "gust",
        "type": "FLOAT"
      },
      {
        "description": "Maximum temperature reported during the day in Fahrenheit to tenths--time of max temp report varies by country and region, so this will sometimes not be the max for the calendar day. Missing = 9999.9",
        "mode": "NULLABLE",
        "name": "max",
        "type": "FLOAT"
      },
      {
        "description": "Blank indicates max temp was taken from the explicit max temp report and not from the 'hourly' data. * indicates max temp was  derived from the hourly data (i.e., highest hourly or synoptic-reported temperature)",
        "mode": "NULLABLE",
        "name": "flag_max",
        "type": "STRING"
      },
      {
        "description": "Minimum temperature reported during the day in Fahrenheit to tenths--time of min temp report varies by country and region, so this will sometimes not be the min for the calendar day. Missing = 9999.9",
        "mode": "NULLABLE",
        "name": "min",
        "type": "FLOAT"
      },
      {
        "description": "Blank indicates min temp was taken from the explicit min temp report and not from the 'hourly' data. * indicates min temp was derived from the hourly data (i.e., lowest hourly or synoptic-reported temperature)",
        "mode": "NULLABLE",
        "name": "flag_min",
        "type": "STRING"
      },
      {
        "description": "Total precipitation (rain and/or melted snow) reported during the day in inches and hundredths; will usually not end with the midnight observation--i.e., may include latter part of previous day.  .00 indicates no measurable precipitation (includes a trace). Missing = 99.99 Note: Many stations do not report '0' on days with no precipitation--therefore, '99.99' will often appear on these days. Also, for example, a station may only report a 6-hour amount for the period during which rain fell. See Flag field for source of data",
        "mode": "NULLABLE",
        "name": "prcp",
        "type": "FLOAT"
      },
      {
        "description": "A = 1 report of 6-hour precipitation amount B = Summation of 2 reports of 6-hour precipitation amount C = Summation of 3 reports of 6-hour precipitation amount D = Summation of 4 reports of 6-hour precipitation amount E = 1 report of 12-hour precipitation amount F = Summation of 2 reports of 12-hour precipitation amount G = 1 report of 24-hour precipitation amount H = Station reported '0' as the amount for the day (eg, from 6-hour reports), but also reported at least one occurrence of precipitation in hourly observations--this could indicate a trace occurred, but should be considered as incomplete data for the day. I = Station did not report any precip data for the day and did not report any occurrences of precipitation in its hourly observations--it's still possible that precip occurred but was not reported",
        "mode": "NULLABLE",
        "name": "flag_prcp",
        "type": "STRING"
      },
      {
        "description": "Snow depth in inches to tenths--last report for the day if reported more thanonce. Missing = 999.9 Note: Most stations do not report '0' ondays with no snow on the ground--therefore, '999.9' will often appear on these days",
        "mode": "NULLABLE",
        "name": "sndp",
        "type": "FLOAT"
      },
      {
        "description": "Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day",
        "mode": "NULLABLE",
        "name": "fog",
        "type": "STRING"
      },
      {
        "description": "Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day",
        "mode": "NULLABLE",
        "name": "rain_drizzle",
        "type": "STRING"
      },
      {
        "description": "Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day",
        "mode": "NULLABLE",
        "name": "snow_ice_pellets",
        "type": "STRING"
      },
      {
        "description": "Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day",
        "mode": "NULLABLE",
        "name": "hail",
        "type": "STRING"
      },
      {
        "description": "Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day",
        "mode": "NULLABLE",
        "name": "thunder",
        "type": "STRING"
      },
      {
        "description": "Indicators (1 = yes, 0 = no/not reported) for the occurrence during the day",
        "mode": "NULLABLE",
        "name": "tornado_funnel_cloud",
        "type": "STRING"
      }
    ]
  },
  "selfLink": "https://bigquery.googleapis.com/bigquery/v2/projects/bigquery-public-data/datasets/noaa_gsod/tables/gsod2025",
  "tableReference": {
    "datasetId": "noaa_gsod",
    "projectId": "bigquery-public-data",
    "tableId": "gsod2025"
  },
  "type": "TABLE"
}
"""

# bq show --format=prettyjson bigquery-public-data:ghcn_d.ghcnd_2025
GHCND_DS_SCHEMA = """
{
  "creationTime": "1735871501647",
  "etag": "axXvC+wj/H5E+I1D+dFEig==",
  "id": "bigquery-public-data:ghcn_d.ghcnd_2025",
  "kind": "bigquery#table",
  "lastModifiedTime": "1763360917481",
  "location": "US",
  "numActiveLogicalBytes": "3098123624",
  "numActivePhysicalBytes": "657487989",
  "numBytes": "3098123624",
  "numCurrentPhysicalBytes": "87371039",
  "numLongTermBytes": "0",
  "numLongTermLogicalBytes": "0",
  "numLongTermPhysicalBytes": "0",
  "numRows": "26803823",
  "numTimeTravelPhysicalBytes": "570116950",
  "numTotalLogicalBytes": "3098123624",
  "numTotalPhysicalBytes": "657487989",
  "schema": {
    "fields": [
      {
        "description": "",
        "mode": "REQUIRED",
        "name": "id",
        "type": "STRING"
      },
      {
        "description": "",
        "mode": "NULLABLE",
        "name": "date",
        "type": "DATE"
      },
      {
        "description": "",
        "mode": "NULLABLE",
        "name": "element",
        "type": "STRING"
      },
      {
        "description": "",
        "mode": "NULLABLE",
        "name": "value",
        "type": "FLOAT"
      },
      {
        "description": "",
        "mode": "NULLABLE",
        "name": "mflag",
        "type": "STRING"
      },
      {
        "description": "",
        "mode": "NULLABLE",
        "name": "qflag",
        "type": "STRING"
      },
      {
        "description": "",
        "mode": "NULLABLE",
        "name": "sflag",
        "type": "STRING"
      },
      {
        "description": "",
        "mode": "NULLABLE",
        "name": "time",
        "type": "STRING"
      },
      {
        "description": "Source ",
        "mode": "NULLABLE",
        "name": "source_url",
        "type": "STRING"
      },
      {
        "description": "Load time for this data row",
        "mode": "NULLABLE",
        "name": "etl_timestamp",
        "type": "TIMESTAMP"
      }
    ]
  },
  "selfLink": "https://bigquery.googleapis.com/bigquery/v2/projects/bigquery-public-data/datasets/ghcn_d/tables/ghcnd_2025",
  "tableReference": {
    "datasetId": "ghcn_d",
    "projectId": "bigquery-public-data",
    "tableId": "ghcnd_2025"
  },
  "type": "TABLE"
}
"""