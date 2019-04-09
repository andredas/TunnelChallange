/**
 * @license
 * Copyright Akveo. All Rights Reserved.
 * Licensed under the MIT License. See License.txt in the project root for license information.
 */
import { APP_BASE_HREF } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { CoreModule } from './@core/core.module';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { ThemeModule } from './@theme/theme.module';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { SystemOverviewComponent } from './pages/dashboard/system-overview/system-overview.component';
import { ControlPanelComponent } from './pages/dashboard/control-panel/control-panel.component';
import { MapOverviewComponent } from './pages/dashboard/map-overview/map-overview.component';
import { NotificationCenterComponent } from './pages/dashboard/notification-center/notification-center.component';
import { DetailOverviewComponent } from './pages/dashboard/detail-overview/detail-overview.component';

@NgModule({
  declarations: [AppComponent, SystemOverviewComponent, ControlPanelComponent, MapOverviewComponent, NotificationCenterComponent, DetailOverviewComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AppRoutingModule,

    NgbModule.forRoot(),
    ThemeModule.forRoot(),
    CoreModule.forRoot(),
  ],
  bootstrap: [AppComponent],
  providers: [
    { provide: APP_BASE_HREF, useValue: '/' },
  ],
})
export class AppModule {
}
