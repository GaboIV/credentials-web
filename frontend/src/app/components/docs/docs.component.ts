import { Component } from '@angular/core';
import { CredentialsService } from '../../services/credentials.service';
import { CommonModule } from '@angular/common';
import { Credential } from '../../models/Credential';

@Component({
  selector: 'app-docs',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './docs.component.html',
  styleUrl: './docs.component.css'
})
export class DocsComponent {
  credentials: Credential[] = [];
  copiedId: number | null = null;

  constructor(private credentialsService: CredentialsService) { }

  ngOnInit(): void {
    this.loadCredentials();
  }

  loadCredentials(): void {
    this.credentialsService.getCredentials().subscribe({
      next: (response) => {
        this.credentials = response.credentials;
      },
      error: (err) => {
        console.error('Error loading credentials:', err);
      }
    });
  }

  copyToClipboard(value: string): void {
    navigator.clipboard.writeText(value).then(() => {
      this.copiedId = this.credentials.find(c => c.encrypt_value === value)?.id || null;

      setTimeout(() => {
        this.copiedId = null;
      }, 3000);
    }).catch(err => {
      console.error('Error copying to clipboard: ', err);
    });
  }
}
