import { Route, Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: '',
        loadComponent: () => import('./components/main-content/main-content.component').then((c) => c.MainContentComponent),
    },
    {
        path: 'docs',
        loadComponent: () => import('./components/docs/docs.component').then((c) => c.DocsComponent),
    },
    {
        path: 'tutorials',
        loadComponent: () => import('./components/tutorials/tutorials.component').then((c) => c.TutorialsComponent)
    },
];
