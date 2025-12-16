import { css } from '@emotion/css';
import { GrafanaTheme2 } from '@grafana/data';

/**
 * Styles
 */
export const getStyles = (theme: GrafanaTheme2) => {
  return {
    field: css`
      margin: ${theme.spacing(0, 0, 0.5, 0)};
    `,
    controls: css`
      width: 100%;
      display: flex;
      align-items: center;
      flex-wrap: wrap;
    `,
    header: css`
      margin-bottom: ${theme.spacing(1)};
      gap: ${theme.spacing(0.5)};
      display: flex;
    `,
    dragIcon: css`
      color: ${theme.colors.text.disabled};
    `,
  };
};
