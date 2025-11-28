---
title: Business Media
description: Learn how to store base64-encoded media files in Grafana dashboards using the Business Input data source.
keywords:
  - business input
labels:
  products:
    - cloud
    - enterprise
    - oss
---

# Business Media

You can use the Static data source to store any supported base64-encoded media files on your Grafana dashboard.

{{< admonition type="note" >}}
The Static data source works well for files that are not too large. If you receive a `413 Request Entity Too Large` error, you have reached the Grafana limit.

In this case, consider using a database or storage data source. [PostgreSQL is a good choice](https://volkovlabs.io/blog/grafana-postgresql-20230123/).
{{< /admonition >}}

## Fields

Use the String field `img` to store a base64-encoded media file. You can include the definition `data:image/IMAGE-FORMAT;base64,ENCODED-CONTENT` or omit it.
