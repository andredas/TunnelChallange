import { Component, OnDestroy } from '@angular/core';
import { NbThemeService } from '@nebular/theme';
import { takeWhile } from 'rxjs/operators' ;

interface CardSettings {
  title: string;
  iconClass: string;
  type: string;
  on: boolean;
}

@Component({
  selector: 'ngx-control-panel',
  templateUrl: './control-panel.component.html',
  styleUrls: ['./control-panel.component.scss']
})

export class ControlPanelComponent implements OnDestroy {
	
	private warning_on = false;
	private error_on = false;
	
	private alive = true;
	
	warningCard: CardSettings = {
		title: 'Warning',
		iconClass: 'ion-alert-circled',
		type: 'primary',
		on: this.warning_on,
	};
	
	dangerCard: CardSettings = {
		title: 'Closed',
		iconClass: 'ion-close-round',
		type: 'primary',
		on: this.error_on,
	};
	
	
	statusCards: string;
	  
	commonStatusCardsSet: CardSettings[] = [
		this.dangerCard,
		this.warningCard,
	];
	
	statusCardsByThemes: {
		default: CardSettings[];
		cosmic: CardSettings[];
		corporate: CardSettings[];
	} = {
		default: this.commonStatusCardsSet,
		cosmic: this.commonStatusCardsSet,
		corporate: [
			  {
				  ...this.dangerCard,
				  type: 'danger',
			  },
			  {
				...this.warningCard,
				type: 'warning',
			  },
			  
			],
	};
	  
	constructor(private themeService: NbThemeService) {
			this.themeService.getJsTheme()
			.pipe(takeWhile(() => this.alive))
			.subscribe(theme => {
				this.statusCards = this.statusCardsByThemes[theme.name];
			});
	}
	onClick(title, on){
		if(title == "Warning"){
			// Warning
			if(!this.warning_on){
				console.log("Tunnel gevaar aan!");
			} else {
				console.log("Tunnel gevaar uit.");
			}
			this.warning_on = !this.warning_on;
		} else {
			// Closed
			if(!this.error_on){
				console.log("Tunnel gesloten!");
			} else {
				console.log("Tunnel open.");
			}
			this.error_on = !this.error_on;
		}
		
	}

  ngOnDestroy() {
    this.alive = false;
  }


}
