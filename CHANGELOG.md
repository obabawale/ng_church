# Change Log
All notable changes to this project will be documented in this file.

## 2017-05-04
### Change
* Upgrade from Odoo version 9 to 10.0
## 2017-05-03
### Add
* Add actions.xml file, this is to serve as central container of all actions
* Add menus.xml file, this is to serve as central container of all menus

_Even bad code can function. But if code isn't clean, it can bring a development organization to its knees_

### Changed
* Rewrite ng_church_church.donation model and rename class name to camel case _Donation_
* Rewrite ng_church_tithes_offerings model and rename class name to camel case _TithesAndOffering_
* Fixed Errors returning when trying to generate invoice
