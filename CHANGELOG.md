# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2024-09-08

### Added

- Widget versioning support via the change_phoebus_version method and optional files in ~/.phoebusgen
- More tests

### Changed

- line_color and predefined_line_color to check the version for the Group widget

### Fixed

- Missing Color property on the XY Plot widget

## [2.8.0] - 2024-09-08

### Added

- Full property support for image widget
- Full property support for strip chart widget
- Full property support for XY plot widget
- This CHANGELOG file to hopefully serve as an evolving example of a
  standardized open source project CHANGELOG.

### Changed

- Widget base class now inherits from a shared Generic class which is also
  used for new classes StripChartTrace, XYPlotTrace, StripChartYAxis, etc.
- Switched from versioneer to setuptools_scm for package versioning
- Switched from setup.py to pyproject.toml

### Removed

- setup.py and setup.cfg files in favor of pyproject.toml

### Fixed

- Bug in symbols property, only could have one symbol previously
- Missing line_color support for group widget since phoebus v4.7.3

## [2.7.0] - 2023-09-18

### Added

- Ability to use color as value in rules

### Fixed

- Bug in items property, only could have one item previously

## [2.6.2] - 2023-08-01

### Fixed

- Bug in confirmation dialog for action button

## [2.6.1] - 2023-06-07

### Added

- Execute script methods for the action button widget

## [2.6.0] - 2023-06-05

### Added

- Alarm border property to text update widget

## [2.5.1] - 2023-04-13

### Changed

- Confirmed github workflow for pip package upload

## [2.5.0] - 2023-04-13

### Fixed

- Version tag should be x.x.x

## [2.5] - 2023-04-13

### Added

- precommit to repository

### Changed

- Documentation to readthedocs

### Fixed

- Bug in rule support, convert non-string inputs to strings

## [2.4.5] - 2022-07-24

### Added

- Rule and script support for all widgets

## [2.4.4] - 2022-06-27

### Added

- Codacy checks to repository

### Changed

- Use isinstance instead of == for type checks

### Removed

- Unused test file

## [2.4.3] - 2022-06-10

### Added

- Alarm border to action button widget

## [2.4.2] - 2022-05-27

### Added

- Horizontal and vertical alignment to text entry widget

## [2.4.1] - 2022-05-21

### Added

- Interpolation, and cursor support to image widget
- Grid color support to XY plot widget

## [2.4] - 2022-05-21

### Added

- title_font, scale_font, and label_font properties

### Changed

- Moved shared font functions to shared file to help with other font properties

### Fixed

- Bug in predefined font logic, removed the .lower() call on the name string

## [2.3.6] - 2022-05-20

### Added

- time_range property to StripChart widget

## [2.3.5] - 2022-05-19

### Fixed

- Github Action for publishing pip package

## [2.3.4] - 2022-05-19

### Added

- Build sphinx docs Github Action

## [2.3.3] - 2022-05-19

### Added

- Versioneer support
- Github Action to publish pip package
- Python 3.11 to CI

## [2.3.2] - 2021-10-01

### Fixed

- Fix bug in title property where it was thought to be specific to StripChart,
  changed class name and added to XY plot as well

## [2.3.1] - 2021-09-30

### Added

- More documentation

## [2.3.0] - 2021-09-30

### Added

- Full property support for table widget
- Sphinx documentation

## [2.2.0] - 2021-09-28

### Added

- Full property support for LED multi state widget
- Full property support for symbol widget
- Full property support for text symbol widget
- Full property support for scaled slider widget

## [2.1.0] - 2021-09-28

### Added

- Full property support for byte monitor widget
- Full property support for navigation tab widget
- Full property support for tab widget

## [2.0.0] - 2021-09-28

### Added

- Polygon widget
- Polyline widget

### Changed

- Refactored the widget property classes to contain the logic for adding
  XML inside the properties.py file (used to be called property_stubs).

### Removed

- Removed the Property class and private classes in property_stubs.py in favor
  of using classes for each property that are inherited by the widgets that
  use them.

## [1.0.1] - 2021-09-23

### Added

- Macros for open display action

## [1.0.0] - 2021-08-25

### Added

- Support for most widgets but not all properties on all widgets

[unreleased]: https://github.com/als-epics/phoebusgen/compare/3.0.0...HEAD
[3.0.0]: https://github.com/als-epics/phoebusgen/compare/2.8.0...3.0.0
[2.8.0]: https://github.com/als-epics/phoebusgen/compare/2.7.0...2.8.0
[2.7.0]: https://github.com/als-epics/phoebusgen/compare/2.6.2...2.7.0
[2.6.2]: https://github.com/als-epics/phoebusgen/compare/2.6.1...2.6.2
[2.6.1]: https://github.com/als-epics/phoebusgen/compare/2.6.0...2.6.1
[2.6.0]: https://github.com/als-epics/phoebusgen/compare/2.5.1...2.6.0
[2.5.1]: https://github.com/als-epics/phoebusgen/compare/2.5.0...2.5.1
[2.5.0]: https://github.com/als-epics/phoebusgen/compare/2.5...2.5.0
[2.5]: https://github.com/als-epics/phoebusgen/compare/2.4.5...2.5
[2.4.5]: https://github.com/als-epics/phoebusgen/compare/2.4.4...2.4.5
[2.4.4]: https://github.com/als-epics/phoebusgen/compare/2.4.3...2.4.4
[2.4.3]: https://github.com/als-epics/phoebusgen/compare/2.4.2...2.4.3
[2.4.2]: https://github.com/als-epics/phoebusgen/compare/2.4.1...2.4.2
[2.4.1]: https://github.com/als-epics/phoebusgen/compare/2.4...2.4.1
[2.4]: https://github.com/als-epics/phoebusgen/compare/2.3.6...2.4
[2.3.6]: https://github.com/als-epics/phoebusgen/compare/2.3.5...2.3.6
[2.3.5]: https://github.com/als-epics/phoebusgen/compare/2.3.4...2.3.5
[2.3.4]: https://github.com/als-epics/phoebusgen/compare/2.3.3...2.3.4
[2.3.3]: https://github.com/als-epics/phoebusgen/compare/2.3.2...2.3.3
[2.3.2]: https://github.com/als-epics/phoebusgen/compare/2.3.1...2.3.2
[2.3.1]: https://github.com/als-epics/phoebusgen/compare/2.3.0...2.3.1
[2.3.0]: https://github.com/als-epics/phoebusgen/compare/2.2.0...2.3.0
[2.2.0]: https://github.com/als-epics/phoebusgen/compare/2.1.0...2.2.0
[2.1.0]: https://github.com/als-epics/phoebusgen/compare/2.0.0...2.1.0
[2.0.0]: https://github.com/als-epics/phoebusgen/compare/1.0.1...2.0.0
[1.0.1]: https://github.com/als-epics/phoebusgen/compare/1.0.0...1.0.1
[1.0.0]: https://github.com/als-epics/phoebusgen/releases/tag/1.0.0
