import React from 'react';
import {createRoot} from 'react-dom/client';

import {LeadWidget} from './widgets';

const createLeadWidget = () => {
  const rootId = 'lead-widget-root';

  const createWidgetRoot = () => {
    const element = document.createElement('div');
    element.id = rootId;
    return element;
  }
  document.body.appendChild(createWidgetRoot());
  const root = createRoot(document.getElementById(rootId));
  root.render(<LeadWidget/>);
}

(function () {
  createLeadWidget();

})();
