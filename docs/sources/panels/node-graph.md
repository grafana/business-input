---
title: Node Graph
description: Learn how to create node and edge data for testing the Node Graph panel in Grafana.
keywords:
  - business input
labels:
  products:
    - cloud
    - enterprise
    - oss
---

# Node Graph

You can use the Static data source to test graph panels like Node Graph.

## Node Fields

- String field `id` with node ids.
- String field `title` for node names.

## Edge Fields

- String field `id` for edge ids.
- String field `source` for source id.
- String field `target` for target id.
- Number field `mainstat` for the value.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/graph.png" class="border" alt="Graph panels like Node Graph can be tested using Static Data Source." >}}
