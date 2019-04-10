import {Component, OnDestroy} from '@angular/core';


@Component({
  selector: 'ngx-cctv',
  styleUrls: ['./cctv.component.scss'],
  templateUrl: './cctv.component.html',
})

export class CctvComponent implements OnDestroy {

  private alive = true;

  ngOnDestroy() {
    this.alive = false;
  }
}
