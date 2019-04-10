import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ngx-notification-center',
  templateUrl: './notification-center.component.html',
  styleUrls: ['./notification-center.component.scss']
})
export class NotificationCenterComponent implements OnInit {

  info = [{
    type: "info",
    message: "message",
    device:"1",
    timestamp:"time"
  }];
  error = [{
    type: "error",
    message: "message",
    device:"1",
    timestamp:"time"
  }];
  warning = [{
    type: "warning",
    message: "message",
    device:"1",
    timestamp:"time"
  }];

  constructor() { }

  ngOnInit() {
  }

}
