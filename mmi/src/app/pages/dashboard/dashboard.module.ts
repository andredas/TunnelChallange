import { NgModule } from '@angular/core';

import { NgxEchartsModule } from 'ngx-echarts';

import { ThemeModule } from '../../@theme/theme.module';
import { DashboardComponent } from './dashboard.component';
import { RoomsComponent } from './rooms/rooms.component';
import { RoomSelectorComponent } from './rooms/room-selector/room-selector.component';
import { SecurityCamerasComponent } from './security-cameras/security-cameras.component';
import { DetailOverviewComponent } from './detail-overview/detail-overview.component';
import { SystemOverviewComponent } from './system-overview/system-overview.component';
import { MapOverviewComponent } from './map-overview/map-overview.component';
import { NotificationCenterComponent } from './notification-center/notification-center.component';
import { ControlPanelComponent } from './control-panel/control-panel.component';
import { StatusCardComponent } from './status-card/status-card.component';

@NgModule({
  imports: [
    ThemeModule,
    NgxEchartsModule,
  ],
  declarations: [
    DashboardComponent,
    RoomSelectorComponent,
    RoomsComponent,
    SecurityCamerasComponent,
    DetailOverviewComponent,
    SystemOverviewComponent,
    MapOverviewComponent,
    ControlPanelComponent,
    NotificationCenterComponent,
	StatusCardComponent,
  ],
})
export class DashboardModule { }
