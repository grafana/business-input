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

- Use the Time field `time` to store a UTC timestamp.
- Use the String field `message` for the text message.
- Use the String field `level` to define the log level: `info`, `error`, and so on.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/logs.png" class="border" alt="Logs panels to display static logs for development." >}}
