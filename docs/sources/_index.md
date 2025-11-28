---
title: Business Input
description: Learn how to store and emulate data in Grafana using the Business Input data source plugin.
keywords:
  - business input
labels:
  products:
    - cloud
    - enterprise
    - oss
weight: 10
---

# Business Input

The Business Input data source is a plugin for Grafana that allows storing and emulating your data.

## Requirements

- Business Input data source version 5.X requires **Grafana 11** or **Grafana 12**.
- Business Input data source version 4.X requires **Grafana 10.2** or **Grafana 11**.
- Static data source version 3.X requires **Grafana 9.2** or **Grafana 10**.
- Static data source version 2.X requires **Grafana 8.5** or **Grafana 9**.
- Static data source version 1.X requires **Grafana 7.3**.

## Getting started

You can install the Business Input data source from the [Grafana Catalog](https://grafana.com/grafana/plugins/marcusolsson-static-datasource/) or by using the Grafana command line tool.

{{< youtube id="1qYzHfPXJF8" >}}

To install using the command line tool, run the following command:

```sh
grafana cli plugins install marcusolsson-static-datasource
```

## Highlights

- Create static visualizations that do not depend on a specific data source.
- Specify values [manually or by using the **JavaScript Values Editor**](/plugins/business-input/panels/business-charts/).
- Generate data with OpenAI and LLM App.
- Build custom query responses for testing or developing panel plugins.
- Store data and images directly in the dashboard.
- Use variables in text fields.
- Use the Number input for Number fields and the Date Time Picker for Time fields.
- Use the Text Area for String inputs with more than 100 characters.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/dashboard.png" class="border" alt="Display Pie Charts based on the data from the Static Data Source." >}}

## Tutorial

This six-minute tutorial explains what the plugin does and demonstrates how to work with its parameters. You can use the plugin for visualization panel discovery, data storage, and troubleshooting.

{{< admonition type="note" >}}
The video references the plugin using its old name.
{{< /admonition >}}

{{< youtube id="QOV8ECOUjWs" >}}

## Documentation

| Section                      | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| [Provisioning](provisioning) | Learn how to automatically provision the data source. |
| [Variables](variables)       | Learn how to use variables.                           |
| [Panels](panels)             | Learn how to use the data source with panels.             |
| [Release Notes](release)     | Stay up to date with the latest features and updates.        |

## License

Apache License Version 2.0, see [LICENSE](https://github.com/volkovlabs/business-input/blob/main/LICENSE).
