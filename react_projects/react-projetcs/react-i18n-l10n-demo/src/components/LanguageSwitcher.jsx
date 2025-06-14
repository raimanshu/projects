import React from 'react';
import { useTranslation } from 'react-i18next';

const languages = [
  { code: 'en', label: 'English' },
  { code: 'fr', label: 'Français' },
  { code: 'es', label: 'Español' }
];

export default function LanguageSwitcher() {
  const { i18n } = useTranslation();

  return (
    <div>
      {languages.map(({ code, label }) => (
        <button
          key={code}
          onClick={() => i18n.changeLanguage(code)}
          disabled={i18n.language === code}
          style={{ marginRight: 8 }}
        >
          {label}
        </button>
      ))}
    </div>
  );
}
