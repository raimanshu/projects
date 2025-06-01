import { Routes } from '@angular/router';

// import { DashboardModule } from './blueprint-3/views/dashboard/dashboard.module';
// // import { NgModule } from '@angular/core';
// import { Routes, RouterModule } from '@angular/router';
// import { AuthLayoutComponent } from './blueprint-3/shared/components/layouts/auth-layout/auth-layout.component';
// import { BlankLayoutComponent } from './blueprint-3/shared/components/layouts/blank-layout/blank-layout.component';
// import { AdminLayoutSidebarLargeComponent } from './blueprint-3/shared/components/layouts/admin-layout-sidebar-large/admin-layout-sidebar-large.component';
// import { AuthGaurd } from './blueprint-3/shared/services/auth.gaurd';

// export const adminRoutes: Routes = [
//   {
//     path: 'dashboard',
//     loadChildren: () => import('./blueprint-3/views/dashboard/dashboard.module').then(m => m.DashboardModule)
//   },
//   {
//     path: 'uikits',
//     loadChildren: () => import('./blueprint-3/views/ui-kits/ui-kits.module').then(m => m.UiKitsModule)
//   },
//   {
//     path: 'forms',
//     loadChildren: () => import('./blueprint-3/views/forms/forms.module').then(m => m.AppFormsModule)
//   },
//   {
//     path: 'invoice',
//     loadChildren: () => import('./blueprint-3/views/invoice/invoice.module').then(m => m.InvoiceModule)
//   },
//   {
//     path: 'inbox',
//     loadChildren: () => import('./blueprint-3/views/inbox/inbox.module').then(m => m.InboxModule)
//   },
//   {
//     path: 'calendar',
//     loadChildren: () => import('./blueprint-3/views/calendar/calendar.module').then(m => m.CalendarAppModule)
//   },
//   {
//     path: 'chat',
//     loadChildren: () => import('./blueprint-3/views/chat/chat.module').then(m => m.ChatModule)
//   },
//   {
//     path: 'contacts',
//     loadChildren: () => import('./blueprint-3/views/contacts/contacts.module').then(m => m.ContactsModule)
//   },
//   {
//     path: 'tables',
//     loadChildren: () => import('./blueprint-3/views/data-tables/data-tables.module').then(m => m.DataTablesModule)
//   },
//   {
//     path: 'pages',
//     loadChildren: () => import('./blueprint-3/views/pages/pages.module').then(m => m.PagesModule)
//   },
//   {
//       path: 'icons',
//       loadChildren: () => import('./blueprint-3/views/icons/icons.module').then(m => m.IconsModule)
//   }
// ];


export const routes: Routes = [
  {
    path:'home',
    // redirectTo: 'home',
    loadChildren: () => import('./views/module-1/module-1.module').then(m => m.Module1Module)
  },
  {
    path:'dashboard',
    loadChildren: () => import('./views/module-2/module-2.module').then(m => m.Module2Module)
  }
];