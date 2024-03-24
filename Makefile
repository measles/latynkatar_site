extract:
	pybabel extract -F babel.cfg -k "lazy_gettext" -o l10n/messages.pot .

update:
	pybabel update -i l10n/messages.pot -d l10n/

create:
	pybabel init -i l10n/messages.pot -d l10n -l $(LCODE)