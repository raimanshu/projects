import React from 'react';
import { useTranslation } from 'react-i18next';
import './i18n'; // initialize i18n
import LanguageSwitcher from './components/LanguageSwitcher';
import { formatDate, formatCurrency } from './utils/localization';

export default function App() {
  const { t, i18n } = useTranslation();

  const formattedDate = formatDate(new Date(), i18n.language);
  const formattedPrice = formatCurrency(19.99, i18n.language);

  return (
    <div style={{ padding: 20 }}>
      <LanguageSwitcher />
      <h1>{t('welcome')}</h1>
      <p>{t('description')}</p>
      <p>{t('date_label', { date: formattedDate })}</p>
      <p>{t('currency_label', { price: formattedPrice })}</p>
    </div>
  );
}
