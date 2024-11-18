import { Routes } from '@angular/router';
import { authGuard } from './guards/auth.guard';

export const routes: Routes = [
  {
      path: '',
      loadComponent: () => import('./components/main-content/main-content.component').then((c) => c.MainContentComponent),
      canActivate: [authGuard],
  },
  {
      path: 'docs',
      loadComponent: () => import('./components/docs/docs.component').then((c) => c.DocsComponent),
      canActivate: [authGuard],
  },
  {
      path: 'tutorials',
      loadComponent: () => import('./components/tutorials/tutorials.component').then((c) => c.TutorialsComponent),
      canActivate: [authGuard],
  },
  {
      path: 'login',
      loadComponent: () => import('./components/login/login.component').then((c) => c.LoginComponent),
  },
];
