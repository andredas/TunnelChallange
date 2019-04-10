import { NgModule } from '@angular/core';

import { NgxEchartsModule } from 'ngx-echarts';

import { ThemeModule } from '../../@theme/theme.module';

import { CctvComponent } from './cctv.component';

const COMPONENTS = [
  CctvComponent
];

@NgModule({
  imports: [
    ThemeModule,
    NgxEchartsModule,
  ],
  declarations: [
      ...COMPONENTS
  ],
})
export class CctvModule { }
