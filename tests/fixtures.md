not changelog test
.
This is the input Markdown test,
then below add the expected output.

- a [link]
- b [0.0.1][]
* c [1.0.0]

[unused reference]: https://example.com
[0.0.1]: https://example.com
[link]: https://example.com
[1.0.0]: https://example.com
.
This is the input Markdown test,
then below add the expected output.

- a [link]
- b [0.0.1][]

* c [1.0.0]

[0.0.1]: https://example.com

[1.0.0]: https://example.com

[link]: https://example.com
.

correct changelog test
.
# Changelog

## [10.1.0] - 2025-01-01

## [2.10.0] - 2025-01-01

## [2.0.0] - 2025-01-01

## [1.0.10] - 2025-01-01

## [1.0.0] - 2025-01-01

## [0.0.10] - 2025-01-01

## [0.0.2] - 2025-01-01

## [0.0.1] - 2025-01-01

[10.1.0]: https://example.com

[2.10.0]: https://example.com

[2.0.0]: https://example.com

[1.0.10]: https://example.com

[1.0.0]: https://example.com

[0.0.10]: https://example.com

[0.0.2]: https://example.com

[0.0.1]: https://example.com
.
# Changelog

## [10.1.0] - 2025-01-01

## [2.10.0] - 2025-01-01

## [2.0.0] - 2025-01-01

## [1.0.10] - 2025-01-01

## [1.0.0] - 2025-01-01

## [0.0.10] - 2025-01-01

## [0.0.2] - 2025-01-01

## [0.0.1] - 2025-01-01

[10.1.0]: https://example.com

[2.10.0]: https://example.com

[2.0.0]: https://example.com

[1.0.10]: https://example.com

[1.0.0]: https://example.com

[0.0.10]: https://example.com

[0.0.2]: https://example.com

[0.0.1]: https://example.com
.

unsorted changelog test
.
# Changelog

## [10.1.0] - 2025-01-01

## [2.0.0] - 2025-01-01

## [2.10.0] - 2025-01-01

## [1.0.10] - 2025-01-01

## [1.0.0] - 2025-01-01

## [0.0.10] - 2025-01-01

## [0.0.2] - 2025-01-01

## [0.0.1] - 2025-01-01

[0.0.1]: https://example.com
[0.0.2]: https://example.com
[0.0.10]: https://example.com
[1.0.0]: https://example.com
[1.0.10]: https://example.com
[2.0.0]: https://example.com
[2.10.0]: https://example.com
[10.1.0]: https://example.com
.
# Changelog

## [10.1.0] - 2025-01-01

## [2.0.0] - 2025-01-01

## [2.10.0] - 2025-01-01

## [1.0.10] - 2025-01-01

## [1.0.0] - 2025-01-01

## [0.0.10] - 2025-01-01

## [0.0.2] - 2025-01-01

## [0.0.1] - 2025-01-01

[10.1.0]: https://example.com

[2.10.0]: https://example.com

[2.0.0]: https://example.com

[1.0.10]: https://example.com

[1.0.0]: https://example.com

[0.0.10]: https://example.com

[0.0.2]: https://example.com

[0.0.1]: https://example.com
.

extra links changelog test
.
# Changelog

## [1.0.0] - 2025-01-01

### Added

- Commit [JIRA-10]

## [1.1.0][] - 2025-01-01

### Added

- Commit [JIRA-2]
- Commit [JIRA-1]

[JIRA-10]: https://example.com "ticket title"
[JIRA-2]: https://example.com "ticket title"
[JIRA-1]: https://example.com "ticket title"

[2.10.0]: https://example.com
[10.1.0]: https://example.com
.
# Changelog

## [1.0.0] - 2025-01-01

### Added

- Commit [JIRA-10]

## [1.1.0][] - 2025-01-01

### Added

- Commit [JIRA-2]
- Commit [JIRA-1]

[10.1.0]: https://example.com

[2.10.0]: https://example.com

[JIRA-1]: https://example.com "ticket title"

[JIRA-10]: https://example.com "ticket title"

[JIRA-2]: https://example.com "ticket title"
.
