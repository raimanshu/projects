import { ExtraModule } from './views/extra/extra.module';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SharedModule } from './shared/shared.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    // SharedModule
    ExtraModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
