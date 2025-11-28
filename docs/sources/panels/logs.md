---
title: Logs
description: Learn how to create static log data for testing logs panels in Grafana.
keywords:
  - business input
labels:
  products:
    - cloud
    - enterprise
    - oss
---

# Logs

You can use the Static data source to test panels for logs.

## Fields

- Time field `time` to store UTC timestamp.
- String field `message` for the text message.
- String field `level` to defined log level: `info`, `error`, etc.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/logs.png" class="border" alt="Logs panels to display static logs for development." >}}
