---
title: Provisioning
description: Learn how to provision the Business Input data source using YAML configuration files in Grafana.
keywords:
  - business input
  - provisioning
labels:
  products:
    - cloud
    - enterprise
    - oss
weight: 20
---

# Provisioning

Grafana supports managing data sources by adding one or more YAML config files in the `provisioning/datasources` folder.

## Example

Example of provisioning the Static Data Source.

```yaml
datasources:
  - name: Static
    type: marcusolsson-static-datasource
    access: proxy
    isDefault: true
    orgId: 1
    version: 1
    editable: true
    jsonData:
      codeEditorEnabled: true
```

## Data sources

After you provision the data source, it appears in the data sources list.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/datasource.png" class="border" alt="Static Data source does not require any configuration." >}}
