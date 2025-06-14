import { format } from 'date-fns';
import { enUS, fr, es } from 'date-fns/locale';

const localeMap = {
  en: enUS,
  fr,
  es,
};

export function formatDate(date, lang) {
  const locale = localeMap[lang] || enUS;
  return format(date, 'PPP', { locale });
}

export function formatCurrency(amount, lang) {
  let currency = 'USD';
  if (lang === 'fr') currency = 'EUR';
  if (lang === 'es') currency = 'EUR';
  return new Intl.NumberFormat(lang, { style: 'currency', currency }).format(amount);
}
