Title: Red Knot Claude MCPunk Conversation
Date: 2025-03-16 11:00
status: hidden

Conversation for [red knot post]({filename}/red_knot.md).

[See full raw markdown](static/full_red_knot_conversation.md) 


# Setting up Red Knot type checker for project

## Human

Hey buddy can you set up the ~/git/ruff project and show me how to run the red knot type checker. Notably it's still under development, with no published docs I am aware of, so you'll likely need to dig into CI or find documentation that may be written but not yet published (perhaps this is in docstrings, perhaps it doesn't exist).

Ultimately I would like instructions on how to switch from mypy to red knot, so that I can do an early assessment of red knot. You don't need to provide that straight away, just start simple and we'll work towards it together.

Thank you!



## Assistant

 I'll set up the Ruff project and look for information about the Red Knot type checker.

**Tool Use: configure_project**

````json
{
  "root_path": "~/git/ruff",
  "project_name": "ruff_project"
}
````

**Tool Result: configure_project**

````
Project /Users/michael/git/ruff configured with 8552 files.
Files are split into 'chunks' - logical sections like:
- Functions (e.g. 'def my_function')
- Classes (e.g. 'class MyClass')
- Markdown sections (e.g. '# Section')
- Import blocks

After configuring, a common workflow is:
1. list_all_files_in_project to get an overview of the project (with
   an initial limit on the depth of the search)
2. Find files by function/class definition:
   find_files_by_chunk_content(... ["def my_funk"])
3. Find files by function/class usage:
   find_files_by_chunk_content(... ["my_funk"])
4. Determine which chunks in the found files are relevant:
    find_matching_chunks_in_file(...)
5. Get details about the chunks:
   chunk_details(...)

Do not immediately list files or otherwise use the project
unless explicitly told to do so.
````



Let's first look at the project structure to get oriented:

**Tool Use: list_all_files_in_project**

````json
{
  "project_name": "ruff_project",
  "limit_depth_from_root": "1"
}
````

**Tool Result: list_all_files_in_project**

````
.: .editorconfig; .gitattributes; .gitignore; .markdownlint.yaml; .pre-commit-config.yaml; .prettierignore; BREAKING_CHANGES.md; CHANGELOG.md; CODE_OF_CONDUCT.md; CONTRIBUTING.md; Cargo.lock; Cargo.toml; Dockerfile; LICENSE; README.md; SECURITY.md; _typos.toml; clippy.toml; knot.schema.json; mkdocs.insiders.yml; mkdocs.public.yml; mkdocs.template.yml; pyproject.toml; ruff.schema.json; rust-toolchain.toml

````



I see "knot.schema.json" which is promising. Now, let's look for files related to Red Knot:

**Tool Use: find_files_by_chunk_content**

````json
{
  "project_name": "ruff_project",
  "chunk_contents_filter": "[\"red knot\", \"redknot\", \"knot\"]"
}
````

**Tool Result: find_files_by_chunk_content**

````
.: .pre-commit-config.yaml; Cargo.lock; Cargo.toml; _typos.toml; knot.schema.json; pyproject.toml
.github: CODEOWNERS
.github/workflows: ci.yaml; daily_property_tests.yaml; mypy_primer.yaml; sync_typeshed.yaml
crates/red_knot: Cargo.toml; README.md
crates/red_knot/docs: mypy_primer.md; tracing.md
crates/red_knot/src: args.rs; logging.rs; main.rs
crates/red_knot/tests: cli.rs; file_watching.rs
crates/red_knot_project: Cargo.toml
crates/red_knot_project/src: combine.rs; db.rs; lib.rs; metadata.rs; walk.rs
crates/red_knot_project/src/db: changes.rs
crates/red_knot_project/src/metadata: configuration_file.rs; options.rs; pyproject.rs; settings.rs
crates/red_knot_project/src/watch: project_watcher.rs
crates/red_knot_project/tests: check.rs
crates/red_knot_python_semantic: Cargo.toml; mdtest.py
crates/red_knot_python_semantic/resources: README.md
crates/red_knot_python_semantic/resources/mdtest: attributes.md; intersection_types.md; invalid_syntax.md; mdtest_config.md; pep695_type_aliases.md; type_api.md; union_types.md
crates/red_knot_python_semantic/resources/mdtest/annotations: invalid.md; unsupported_special_forms.md; unsupported_type_qualifiers.md
crates/red_knot_python_semantic/resources/mdtest/call: builtins.md; function.md; subclass_of.md
crates/red_knot_python_semantic/resources/mdtest/directives: assert_type.md
crates/red_knot_python_semantic/resources/mdtest/generics: classes.md
crates/red_knot_python_semantic/resources/mdtest/import: conventions.md
crates/red_knot_python_semantic/resources/mdtest/literal: bytes.md
crates/red_knot_python_semantic/resources/mdtest/narrow: isinstance.md
crates/red_knot_python_semantic/resources/mdtest/snapshots: attribute_assignment.md_-_Attribute_assignment_-_Data_descriptors_-_Invalid_`__set__`_method_signature.snap; attribute_assignment.md_-_Attribute_assignment_-_Data_descriptors_-_Invalid_argument_type.snap; attribute_assignment.md_-_Attribute_assignment_-_Instance_attributes_with_class-level_defaults.snap; attribute_assignment.md_-_Attribute_assignment_-_Possibly-unbound_attributes.snap; attribute_assignment.md_-_Attribute_assignment_-_Pure_instance_attributes.snap; attribute_assignment.md_-_Attribute_assignment_-_Setting_attributes_on_union_types.snap; attribute_assignment.md_-_Attribute_assignment_-_Unknown_attributes.snap; attribute_assignment.md_-_Attribute_assignment_-_`ClassVar`s.snap; basic.md_-_Structures_-_Unresolvable_module_import.snap; basic.md_-_Structures_-_Unresolvable_submodule_imports.snap; for.md_-_For_loops_-_Bad_`__getitem__`_method.snap; for.md_-_For_loops_-_Invalid_iterable.snap; for.md_-_For_loops_-_New_over_old_style_iteration_protocol.snap; for.md_-_For_loops_-_No_`__iter__`_method_and_`__getitem__`_is_not_callable.snap; for.md_-_For_loops_-_Possibly-not-callable_`__getitem__`_method.snap; for.md_-_For_loops_-_Possibly_invalid_`__getitem__`_methods.snap; for.md_-_For_loops_-_Possibly_invalid_`__iter__`_methods.snap; for.md_-_For_loops_-_Possibly_invalid_`__next__`_method.snap; for.md_-_For_loops_-_Possibly_unbound_`__iter__`_and_bad_`__getitem__`_method.snap; for.md_-_For_loops_-_Possibly_unbound_`__iter__`_and_possibly_invalid_`__getitem__`.snap; for.md_-_For_loops_-_Possibly_unbound_`__iter__`_and_possibly_unbound_`__getitem__`.snap; for.md_-_For_loops_-_Union_type_as_iterable_where_one_union_element_has_invalid_`__iter__`_method.snap; for.md_-_For_loops_-_Union_type_as_iterable_where_one_union_element_has_no_`__iter__`_method.snap; for.md_-_For_loops_-_With_non-callable_iterator.snap; for.md_-_For_loops_-_`__iter__`_does_not_return_an_iterator.snap; for.md_-_For_loops_-_`__iter__`_method_with_a_bad_signature.snap; for.md_-_For_loops_-_`__iter__`_returns_an_iterator_with_an_invalid_`__next__`_method.snap; instances.md_-_Binary_operations_on_instances_-_Operations_involving_types_with_invalid_`__bool__`_methods.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Basic.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Calls_to_methods.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Different_files.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Different_source_order.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Many_parameters.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Many_parameters_across_multiple_lines.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Many_parameters_with_multiple_invalid_arguments.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Test_calling_a_function_whose_type_is_vendored_from_`typeshed`.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Tests_for_a_variety_of_argument_types_-_Keyword_only_arguments.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Tests_for_a_variety_of_argument_types_-_Mix_of_arguments.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Tests_for_a_variety_of_argument_types_-_One_keyword_argument.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Tests_for_a_variety_of_argument_types_-_Only_positional.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Tests_for_a_variety_of_argument_types_-_Synthetic_arguments.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Tests_for_a_variety_of_argument_types_-_Variadic_arguments.snap; invalid_argument_type.md_-_Invalid_argument_type_diagnostics_-_Tests_for_a_variety_of_argument_types_-_Variadic_keyword_arguments.snap; membership_test.md_-_Comparison___Membership_Test_-_Return_type_that_doesn't_implement_`__bool__`_correctly.snap; no_matching_overload.md_-_No_matching_overload_diagnostics_-_Calls_to_overloaded_functions.snap; not.md_-_Unary_not_-_Object_that_implements_`__bool__`_incorrectly.snap; return_type.md_-_Function_return_type_-_Invalid_conditional_return_type.snap; return_type.md_-_Function_return_type_-_Invalid_implicit_return_type.snap; return_type.md_-_Function_return_type_-_Invalid_return_type.snap; return_type.md_-_Function_return_type_-_Invalid_return_type_in_stub_file.snap; rich_comparison.md_-_Comparison___Rich_Comparison_-_Chained_comparisons_with_objects_that_don't_implement_`__bool__`_correctly.snap; tuples.md_-_Comparison___Tuples_-_Chained_comparisons_with_elements_that_incorrectly_implement_`__bool__`.snap; tuples.md_-_Comparison___Tuples_-_Equality_with_elements_that_incorrectly_implement_`__bool__`.snap; unpacking.md_-_Unpacking_-_Right_hand_side_not_iterable.snap; unpacking.md_-_Unpacking_-_Too_few_values_to_unpack.snap; unpacking.md_-_Unpacking_-_Too_many_values_to_unpack.snap; unresolved_import.md_-_Unresolved_import_diagnostics_-_An_unresolvable_import_that_does_not_use_`from`.snap; unresolved_import.md_-_Unresolved_import_diagnostics_-_Using_`from`_with_a_resolvable_module_but_unresolvable_item.snap; unresolved_import.md_-_Unresolved_import_diagnostics_-_Using_`from`_with_an_unknown_current_module.snap; unresolved_import.md_-_Unresolved_import_diagnostics_-_Using_`from`_with_an_unknown_nested_module.snap; unresolved_import.md_-_Unresolved_import_diagnostics_-_Using_`from`_with_an_unresolvable_module.snap; unresolved_import.md_-_Unresolved_import_diagnostics_-_Using_`from`_with_too_many_leading_dots.snap
crates/red_knot_python_semantic/resources/mdtest/suppressions: knot_ignore.md; no_type_check.md
crates/red_knot_python_semantic/resources/mdtest/type_properties: is_assignable_to.md; is_disjoint_from.md; is_equivalent_to.md; is_fully_static.md; is_gradual_equivalent_to.md; is_single_valued.md; is_singleton.md; is_subtype_of.md; truthiness.md; tuples_containing_never.md
crates/red_knot_python_semantic/src: db.rs; lint.rs; module_name.rs; site_packages.rs; suppression.rs; types.rs
crates/red_knot_python_semantic/src/module_resolver: module.rs; typeshed.rs
crates/red_knot_python_semantic/src/types: class.rs; diagnostic.rs; property_tests.rs
crates/red_knot_python_semantic/tests: mdtest.rs
crates/red_knot_server: Cargo.toml
crates/red_knot_server/src: lib.rs; logging.rs; session.rs
crates/red_knot_server/src/server/api: traits.rs
crates/red_knot_server/src/server/api/notifications: did_change.rs; did_close.rs; did_close_notebook.rs; did_open.rs; did_open_notebook.rs
crates/red_knot_server/src/server/api/requests: diagnostic.rs
crates/red_knot_test: Cargo.toml; README.md
crates/red_knot_test/src: config.rs; db.rs; lib.rs
crates/red_knot_vendored: Cargo.toml; README.md; build.rs
crates/red_knot_vendored/knot_extensions: README.md
crates/red_knot_wasm: Cargo.toml
crates/red_knot_wasm/src: lib.rs
crates/red_knot_wasm/tests: api.rs
crates/ruff_benchmark: Cargo.toml
crates/ruff_benchmark/benches: red_knot.rs
crates/ruff_db/src: testing.rs
crates/ruff_dev: Cargo.toml
crates/ruff_dev/src: generate_all.rs; generate_knot_schema.rs; main.rs
crates/ruff_graph: Cargo.toml
crates/ruff_graph/src: collector.rs; db.rs; resolver.rs
crates/ruff_linter/src: logging.rs
crates/ruff_linter/src/rules/flake8_bandit/snapshots: ruff_linter__rules__flake8_bandit__tests__S704_S704.py.snap
crates/ruff_macros/src: lib.rs
fuzz: Cargo.toml; README.md; init-fuzzer.sh
fuzz/fuzz_targets: red_knot_check_invalid_syntax.rs
python/py-fuzzer: fuzz.py
scripts/knot_benchmark: README.md; pyproject.toml; uv.lock
scripts/knot_benchmark/src/benchmark: cases.py; run.py

````



I can see there's a `crates/red_knot` directory, which suggests this is a Rust implementation of a type checker. Let's examine some key files to better understand how to use it.

Let's first check the Red Knot README:

**Tool Use: chunk_details**

````json
{
  "chunk_id": "crates/red_knot/README.md:chunk0"
}
````

**Tool Result: chunk_details**

````
No matching chunks. Please use other tools to find available chunks.
````





**Tool Use: find_matching_chunks_in_file**

````json
{
  "filter_": "[\"\"]",
  "rel_path": "crates/red_knot/README.md",
  "project_name": "ruff_project"
}
````

**Tool Result: find_matching_chunks_in_file**

````
(2 of 2 chunks)
id=Red Knot_1a6c27a713 (category=markdown section chars=520)
id=Contributing_86d1dddae6 (category=markdown section chars=554)
````





**Tool Use: chunk_details**

````json
{
  "chunk_id": "Red Knot_1a6c27a713"
}
````

**Tool Result: chunk_details**

````
# Red Knot

Red Knot is an extremely fast type checker.
Currently, it is a work-in-progress and not ready for user testing.

Red Knot is designed to prioritize good type inference, even in unannotated code,
and aims to avoid false positives.

While Red Knot will produce similar results to mypy and pyright on many codebases,
100% compatibility with these tools is a non-goal.
On some codebases, Red Knot's design decisions lead to different outcomes
than you would get from running one of these more established tools.
````





**Tool Use: chunk_details**

````json
{
  "chunk_id": "Contributing_86d1dddae6"
}
````

**Tool Result: chunk_details**

````
## Contributing

Core type checking tests are written as Markdown code blocks.
They can be found in [`red_knot_python_semantic/resources/mdtest`][resources-mdtest].
See [`red_knot_test/README.md`][mdtest-readme] for more information
on the test framework itself.

The list of open issues can be found [here][open-issues].

[mdtest-readme]: ../red_knot_test/README.md
[open-issues]: https://github.com/astral-sh/ruff/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20label%3Ared-knot
[resources-mdtest]: ../red_knot_python_semantic/resources/mdtest
````





Let's look at how Red Knot is configured in pyproject.toml:

**Tool Use: find_matching_chunks_in_file**

````json
{
  "filter_": "[\"knot\"]",
  "rel_path": "pyproject.toml",
  "project_name": "ruff_project"
}
````

**Tool Result: find_matching_chunks_in_file**

````
(1 of 1 chunks)
id=whole_file_77f3f357ee (category=whole_file chars=4092)
````







**Tool Use: chunk_details**

````json
{
  "chunk_id": "whole_file_77f3f357ee"
}
````

**Tool Result: chunk_details**

````
[build-system]
requires = ["maturin>=1.0,<2.0"]
build-backend = "maturin"

[project]
name = "ruff"
version = "0.11.0"
description = "An extremely fast Python linter and code formatter, written in Rust."
authors = [{ name = "Astral Software Inc.", email = "hey@astral.sh" }]
readme = "README.md"
requires-python = ">=3.7"
license = { file = "LICENSE" }
keywords = [
    "automation",
    "flake8",
    "pycodestyle",
    "pyflakes",
    "pylint",
    "clippy",
]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Rust",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Quality Assurance",
]

[project.urls]
Repository = "https://github.com/astral-sh/ruff"
Documentation = "https://docs.astral.sh/ruff/"
Changelog = "https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md"

[tool.maturin]
bindings = "bin"
manifest-path = "crates/ruff/Cargo.toml"
module-name = "ruff"
python-source = "python"
strip = true
exclude = [
    "crates/ruff_linter/resources/test/fixtures/**/*",
    "crates/ruff_linter/src/rules/*/snapshots/**/*"
]
include = [
    "rust-toolchain.toml"
]

[tool.ruff]
target-version = "py38"
extend-exclude = [
    "crates/red_knot_vendored/vendor/",
    "crates/ruff/resources/",
    "crates/ruff_linter/resources/",
    "crates/ruff_python_formatter/resources/",
    "crates/ruff_python_parser/resources/"
]

[tool.ruff.lint]
select = [
    "E", # pycodestyle (error)
    "F", # pyflakes
    "B", # bugbear
    "B9",
    "C4", # flake8-comprehensions
    "SIM", # flake8-simplify
    "I", # isort
    "UP", # pyupgrade
    "PIE", # flake8-pie
    "PGH", # pygrep-hooks
    "PYI", # flake8-pyi
    "RUF",
]

ignore = [
    # only relevant if you run a script with `python -0`,
    # which seems unlikely for any of the scripts in this repo
    "B011",
    # Leave it to the formatter to split long lines and
    # the judgement of all of us.
    "E501"
]

[tool.ruff.lint.isort]
required-imports = ["from __future__ import annotations"]

[tool.black]
force-exclude = '''
/(
  | crates/red_knot_vendored/vendor
  | crates/ruff_linter/resources
  | crates/ruff_python_formatter/resources
  | crates/ruff_python_parser/resources
)/
'''

[tool.rooster]
major_labels = []  # Ruff never uses the major version number
minor_labels = ["breaking"]   # Bump the minor version on breaking changes

changelog_ignore_labels = ["internal", "ci", "red-knot", "testing"]

changelog_sections.breaking = "Breaking changes"
changelog_sections.preview = "Preview features"
changelog_sections.bug = "Bug fixes"
changelog_sections.rule = "Rule changes"
changelog_sections.diagnostics = "Rule changes"
changelog_sections.docstring = "Rule changes"
changelog_sections.fixes = "Rule changes"
changelog_sections.isort = "Rule changes"
changelog_sections.performance = "Performance"
changelog_sections.formatter = "Formatter"
changelog_sections.server = "Server"
changelog_sections.cli = "CLI"
changelog_sections.configuration = "Configuration"
changelog_sections.documentation = "Documentation"
changelog_sections.__unknown__ = "Other changes"

# We exclude contributors from the CHANGELOG file
# Generate separately with `rooster contributors` for the GitHub release page
changelog_contributors = false

version_files = [
    "README.md",
    "docs/integrations.md",
    "docs/tutorial.md",
    "crates/ruff/Cargo.toml",
    "crates/ruff_linter/Cargo.toml",
    "crates/ruff_wasm/Cargo.toml",
    "scripts/benchmarks/pyproject.toml",
]
````






Now, let's look at the documentation for setting up Red Knot. Let's check CI files to see how it's being used there:

**Tool Use: find_matching_chunks_in_file**

````json
{
  "filter_": "[\"knot\"]",
  "rel_path": ".github/workflows/ci.yaml",
  "project_name": "ruff_project"
}
````

**Tool Result: find_matching_chunks_in_file**

````
(1 of 3 chunks)
id=whole_file_part1_9c8c4cc8a6 (category=whole_file chars=9985)
````






**Tool Use: chunk_details**

````json
{
  "chunk_id": "whole_file_part1_9c8c4cc8a6"
}
````

**Tool Result: chunk_details**

````
[This is a subsection of the chunk. Other parts contain the rest of the chunk]

name: CI

permissions: {}

on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.ref_name }}-${{ github.event.pull_request.number || github.sha }}
  cancel-in-progress: true

env:
  CARGO_INCREMENTAL: 0
  CARGO_NET_RETRY: 10
  CARGO_TERM_COLOR: always
  RUSTUP_MAX_RETRIES: 10
  PACKAGE_NAME: ruff
  PYTHON_VERSION: "3.12"

jobs:
  determine_changes:
    name: "Determine changes"
    runs-on: ubuntu-latest
    outputs:
      # Flag that is raised when any code that affects parser is changed
      parser: ${{ steps.changed.outputs.parser_any_changed }}
      # Flag that is raised when any code that affects linter is changed
      linter: ${{ steps.changed.outputs.linter_any_changed }}
      # Flag that is raised when any code that affects formatter is changed
      formatter: ${{ steps.changed.outputs.formatter_any_changed }}
      # Flag that is raised when any code is changed
      # This is superset of the linter and formatter
      code: ${{ steps.changed.outputs.code_any_changed }}
      # Flag that is raised when any code that affects the fuzzer is changed
      fuzz: ${{ steps.changed.outputs.fuzz_any_changed }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: false

      - uses: tj-actions/changed-files@v45
        id: changed
        with:
          files_yaml: |
            parser:
              - Cargo.toml
              - Cargo.lock
              - crates/ruff_python_trivia/**
              - crates/ruff_source_file/**
              - crates/ruff_text_size/**
              - crates/ruff_python_ast/**
              - crates/ruff_python_parser/**
              - python/py-fuzzer/**
              - .github/workflows/ci.yaml

            linter:
              - Cargo.toml
              - Cargo.lock
              - crates/**
              - "!crates/red_knot*/**"
              - "!crates/ruff_python_formatter/**"
              - "!crates/ruff_formatter/**"
              - "!crates/ruff_dev/**"
              - scripts/*
              - python/**
              - .github/workflows/ci.yaml

            formatter:
              - Cargo.toml
              - Cargo.lock
              - crates/ruff_python_formatter/**
              - crates/ruff_formatter/**
              - crates/ruff_python_trivia/**
              - crates/ruff_python_ast/**
              - crates/ruff_source_file/**
              - crates/ruff_python_index/**
              - crates/ruff_text_size/**
              - crates/ruff_python_parser/**
              - crates/ruff_dev/**
              - scripts/*
              - python/**
              - .github/workflows/ci.yaml

            fuzz:
              - fuzz/Cargo.toml
              - fuzz/Cargo.lock
              - fuzz/fuzz_targets/**

            code:
              - "**/*"
              - "!**/*.md"
              - "crates/red_knot_python_semantic/resources/mdtest/**/*.md"
              - "!docs/**"
              - "!assets/**"

  cargo-fmt:
    name: "cargo fmt"
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - name: "Install Rust toolchain"
        run: rustup component add rustfmt
      - run: cargo fmt --all --check

  cargo-clippy:
    name: "cargo clippy"
    runs-on: ubuntu-latest
    needs: determine_changes
    if: ${{ needs.determine_changes.outputs.code == 'true' || github.ref == 'refs/heads/main' }}
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: Swatinem/rust-cache@v2
      - name: "Install Rust toolchain"
        run: |
          rustup component add clippy
          rustup target add wasm32-unknown-unknown
      - name: "Clippy"
        run: cargo clippy --workspace --all-targets --all-features --locked -- -D warnings
      - name: "Clippy (wasm)"
        run: cargo clippy -p ruff_wasm -p red_knot_wasm --target wasm32-unknown-unknown --all-features --locked -- -D warnings

  cargo-test-linux:
    name: "cargo test (linux)"
    runs-on: depot-ubuntu-22.04-16
    needs: determine_changes
    if: ${{ !contains(github.event.pull_request.labels.*.name, 'no-test') && (needs.determine_changes.outputs.code == 'true' || github.ref == 'refs/heads/main') }}
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: Swatinem/rust-cache@v2
      - name: "Install Rust toolchain"
        run: rustup show
      - name: "Install mold"
        uses: rui314/setup-mold@v1
      - name: "Install cargo nextest"
        uses: taiki-e/install-action@v2
        with:
          tool: cargo-nextest
      - name: "Install cargo insta"
        uses: taiki-e/install-action@v2
        with:
          tool: cargo-insta
      - name: "Run tests"
        shell: bash
        env:
          NEXTEST_PROFILE: "ci"
        run: cargo insta test --all-features --unreferenced reject --test-runner nextest

      # Check for broken links in the documentation.
      - run: cargo doc --all --no-deps
        env:
          RUSTDOCFLAGS: "-D warnings"
      # Use --document-private-items so that all our doc comments are kept in
      # sync, not just public items. Eventually we should do this for all
      # crates; for now add crates here as they are warning-clean to prevent
      # regression.
      - run: cargo doc --no-deps -p red_knot_python_semantic -p red_knot -p red_knot_test -p ruff_db --document-private-items
        env:
          # Setting RUSTDOCFLAGS because `cargo doc --check` isn't yet implemented (https://github.com/rust-lang/cargo/issues/10025).
          RUSTDOCFLAGS: "-D warnings"
      - uses: actions/upload-artifact@v4
        with:
          name: ruff
          path: target/debug/ruff

  cargo-test-linux-release:
    name: "cargo test (linux, release)"
    runs-on: depot-ubuntu-22.04-16
    needs: determine_changes
    if: ${{ !contains(github.event.pull_request.labels.*.name, 'no-test') && (needs.determine_changes.outputs.code == 'true' || github.ref == 'refs/heads/main') }}
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: Swatinem/rust-cache@v2
      - name: "Install Rust toolchain"
        run: rustup show
      - name: "Install mold"
        uses: rui314/setup-mold@v1
      - name: "Install cargo nextest"
        uses: taiki-e/install-action@v2
        with:
          tool: cargo-nextest
      - name: "Install cargo insta"
        uses: taiki-e/install-action@v2
        with:
          tool: cargo-insta
      - name: "Run tests"
        shell: bash
        env:
          NEXTEST_PROFILE: "ci"
        run: cargo insta test --release --all-features --unreferenced reject --test-runner nextest

  cargo-test-windows:
    name: "cargo test (windows)"
    runs-on: github-windows-2025-x86_64-16
    needs: determine_changes
    if: ${{ !contains(github.event.pull_request.labels.*.name, 'no-test') && (needs.determine_changes.outputs.code == 'true' || github.ref == 'refs/heads/main') }}
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: Swatinem/rust-cache@v2
      - name: "Install Rust toolchain"
        run: rustup show
      - name: "Install cargo nextest"
        uses: taiki-e/install-action@v2
        with:
          tool: cargo-nextest
      - name: "Run tests"
        shell: bash
        env:
          NEXTEST_PROFILE: "ci"
          # Workaround for <https://github.com/nextest-rs/nextest/issues/1493>.
          RUSTUP_WINDOWS_PATH_ADD_BIN: 1
        run: |
          cargo nextest run --all-features --profile ci
          cargo test --all-features --doc

  cargo-test-wasm:
    name: "cargo test (wasm)"
    runs-on: ubuntu-latest
    needs: determine_changes
    if: ${{ !contains(github.event.pull_request.labels.*.name, 'no-test') && (needs.determine_changes.outputs.code == 'true' || github.ref == 'refs/heads/main') }}
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: Swatinem/rust-cache@v2
      - name: "Install Rust toolchain"
        run: rustup target add wasm32-unknown-unknown
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"
          cache-dependency-path: playground/package-lock.json
      - uses: jetli/wasm-pack-action@v0.4.0
        with:
          version: v0.13.1
      - name: "Test ruff_wasm"
        run: |
          cd crates/ruff_wasm
          wasm-pack test --node
      - name: "Test red_knot_wasm"
        run: |
          cd crates/red_knot_wasm
          wasm-pack test --node

  cargo-build-release:
    name: "cargo build (release)"
    runs-on: macos-latest
    if: ${{ github.ref == 'refs/heads/main' }}
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: Swatinem/rust-cache@v2
      - name: "Install Rust toolchain"
        run: rustup show
      - name: "Install mold"
        uses: rui314/setup-mold@v1
      - name: "Build"
        run: cargo build --release --locked

  cargo-build-msrv:
    name: "cargo build (msrv)"
    runs-on: depot-ubuntu-latest-8
    needs: determine_changes
    if: ${{ !contains(github.event.pull_request.labels.*.name, 'no-test') && (needs.determine_changes.outputs.code == 'true' || github.ref == 'refs/heads/main') }}
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: false
      - uses: SebRollen/toml-action@v1.2.0
        id: msrv
        with:
          file: "Cargo.toml"
          field: "workspace.package.rust-version"
````






Let's look at the knot.schema.json file to understand the configuration options:

**Tool Use: find_matching_chunks_in_file**

````json
{
  "filter_": "[\"\"]",
  "rel_path": "knot.schema.json",
  "project_name": "ruff_project"
}
````

**Tool Result: find_matching_chunks_in_file**

````
(4 of 4 chunks)
id=whole_file_part1_dcac4f951b (category=whole_file chars=9940)
id=whole_file_part2_1dfa38bcca (category=whole_file chars=9987)
id=whole_file_part3_a115d7e27b (category=whole_file chars=9868)
id=whole_file_part4_4dc68d0fb1 (category=whole_file chars=6585)
````









**Tool Use: chunk_details**

````json
{
  "chunk_id": "whole_file_part1_dcac4f951b"
}
````

**Tool Result: chunk_details**

````
[This is a subsection of the chunk. Other parts contain the rest of the chunk]

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Options",
  "description": "The options for the project.",
  "type": "object",
  "properties": {
    "environment": {
      "description": "Configures the type checking environment.",
      "anyOf": [
        {
          "$ref": "#/definitions/EnvironmentOptions"
        },
        {
          "type": "null"
        }
      ]
    },
    "rules": {
      "description": "Configures the enabled lints and their severity.",
      "anyOf": [
        {
          "$ref": "#/definitions/Rules"
        },
        {
          "type": "null"
        }
      ]
    },
    "src": {
      "anyOf": [
        {
          "$ref": "#/definitions/SrcOptions"
        },
        {
          "type": "null"
        }
      ]
    },
    "terminal": {
      "anyOf": [
        {
          "$ref": "#/definitions/TerminalOptions"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "additionalProperties": false,
  "definitions": {
    "DiagnosticFormat": {
      "description": "The diagnostic output format.",
      "oneOf": [
        {
          "description": "The default full mode will print \"pretty\" diagnostics.\n\nThat is, color will be used when printing to a `tty`. Moreover, diagnostic messages may include additional context and annotations on the input to help understand the message.",
          "type": "string",
          "enum": [
            "full"
          ]
        },
        {
          "description": "Print diagnostics in a concise mode.\n\nThis will guarantee that each diagnostic is printed on a single line. Only the most important or primary aspects of the diagnostic are included. Contextual information is dropped.\n\nThis may use color when printing to a `tty`.",
          "type": "string",
          "enum": [
            "concise"
          ]
        }
      ]
    },
    "EnvironmentOptions": {
      "type": "object",
      "properties": {
        "extra-paths": {
          "description": "List of user-provided paths that should take first priority in the module resolution. Examples in other type checkers are mypy's MYPYPATH environment variable, or pyright's stubPath configuration setting.",
          "type": [
            "array",
            "null"
          ],
          "items": {
            "type": "string"
          }
        },
        "python": {
          "description": "Path to the Python installation from which Red Knot resolves type information and third-party dependencies.\n\nRed Knot will search in the path's `site-packages` directories for type information and third-party imports.\n\nThis option is commonly used to specify the path to a virtual environment.",
          "type": [
            "string",
            "null"
          ]
        },
        "python-platform": {
          "description": "Specifies the target platform that will be used to execute the source code. If specified, Red Knot will tailor its use of type stub files, which conditionalize type definitions based on the platform.\n\nIf no platform is specified, knot will use `all` or the current platform in the LSP use case.",
          "anyOf": [
            {
              "$ref": "#/definitions/PythonPlatform"
            },
            {
              "type": "null"
            }
          ]
        },
        "python-version": {
          "description": "Specifies the version of Python that will be used to execute the source code. The version should be specified as a string in the format `M.m` where `M` is the major version and `m` is the minor (e.g. \"3.0\" or \"3.6\"). If a version is provided, knot will generate errors if the source code makes use of language features that are not supported in that version. It will also tailor its use of type stub files, which conditionalizes type definitions based on the version.",
          "anyOf": [
            {
              "$ref": "#/definitions/PythonVersion"
            },
            {
              "type": "null"
            }
          ]
        },
        "typeshed": {
          "description": "Optional path to a \"typeshed\" directory on disk for us to use for standard-library types. If this is not provided, we will fallback to our vendored typeshed stubs for the stdlib, bundled as a zip file in the binary",
          "type": [
            "string",
            "null"
          ]
        }
      },
      "additionalProperties": false
    },
    "Level": {
      "oneOf": [
        {
          "title": "Ignore",
          "description": "The lint is disabled and should not run.",
          "type": "string",
          "enum": [
            "ignore"
          ]
        },
        {
          "title": "Warn",
          "description": "The lint is enabled and diagnostic should have a warning severity.",
          "type": "string",
          "enum": [
            "warn"
          ]
        },
        {
          "title": "Error",
          "description": "The lint is enabled and diagnostics have an error severity.",
          "type": "string",
          "enum": [
            "error"
          ]
        }
      ]
    },
    "PythonPlatform": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "description": "Do not make any assumptions about the target platform.",
          "const": "all"
        },
        {
          "description": "Darwin",
          "const": "darwin"
        },
        {
          "description": "Linux",
          "const": "linux"
        },
        {
          "description": "Windows",
          "const": "win32"
        }
      ]
    },
    "PythonVersion": {
      "anyOf": [
        {
          "type": "string",
          "pattern": "^\\d+\\.\\d+$"
        },
        {
          "description": "Python 3.7",
          "const": "3.7"
        },
        {
          "description": "Python 3.8",
          "const": "3.8"
        },
        {
          "description": "Python 3.9",
          "const": "3.9"
        },
        {
          "description": "Python 3.10",
          "const": "3.10"
        },
        {
          "description": "Python 3.11",
          "const": "3.11"
        },
        {
          "description": "Python 3.12",
          "const": "3.12"
        },
        {
          "description": "Python 3.13",
          "const": "3.13"
        }
      ]
    },
    "Rules": {
      "type": "object",
      "properties": {
        "byte-string-type-annotation": {
          "title": "detects byte strings in type annotation positions",
          "description": "## What it does\nChecks for byte-strings in type annotation positions.\n\n## Why is this bad?\nStatic analysis tools like Red Knot can't analyse type annotations that use byte-string notation.\n\n## Examples\n```python\ndef test(): -> b\"int\":\n    ...\n```\n\nUse instead:\n```python\ndef test(): -> \"int\":\n    ...\n```",
          "default": "error",
          "oneOf": [
            {
              "$ref": "#/definitions/Level"
            }
          ]
        },
        "call-non-callable": {
          "title": "detects calls to non-callable objects",
          "description": "## What it does\nChecks for calls to non-callable objects.\n\n## Why is this bad?\nCalling a non-callable object will raise a `TypeError` at runtime.\n\n## Examples\n```python\n4()  # TypeError: 'int' object is not callable\n```",
          "default": "error",
          "oneOf": [
            {
              "$ref": "#/definitions/Level"
            }
          ]
        },
        "call-possibly-unbound-method": {
          "title": "detects calls to possibly unbound methods",
          "description": "## What it does\nChecks for calls to possibly unbound methods.\n\nTODO #14889",
          "default": "warn",
          "oneOf": [
            {
              "$ref": "#/definitions/Level"
            }
          ]
        },
        "conflicting-declarations": {
          "title": "detects conflicting declarations",
          "description": "TODO #14889",
          "default": "error",
          "oneOf": [
            {
              "$ref": "#/definitions/Level"
            }
          ]
        },
        "conflicting-metaclass": {
          "title": "detects conflicting metaclasses",
          "description": "TODO #14889",
          "default": "error",
          "oneOf": [
            {
              "$ref": "#/definitions/Level"
            }
          ]
        },
        "cyclic-class-definition": {
          "title": "detects cyclic class definitions",
          "description": "## What it does\nChecks for class definitions with a cyclic inheritance chain.\n\n## Why is it bad?\nTODO #14889",
          "default": "error",
          "oneOf": [
            {
              "$ref": "#/definitions/Level"
            }
          ]
        },
        "division-by-zero": {
          "title": "detects division by zero",
          "description": "## What it does\nIt detects division by zero.\n\n## Why is this bad?\nDividing by zero raises a `ZeroDivisionError` at runtime.\n\n## Examples\n```python\n5 / 0\n```",
          "default": "error",
          "oneOf": [
            {
              "$ref": "#/definitions/Level"
            }
          ]
        },
        "duplicate-base": {
          "title": "detects class definitions with duplicate bases",
          "description": "TODO #14889",
          "default": "error",
          "oneOf": [
            {
              "$ref": "#/definitions/Level"
            }
          ]
        },
        "escape-character-in-forward-annotation": {
          "title": "detects forward type annotations with escape characters",
          "description": "TODO #14889",
          "default": "error",
          "oneOf": [
            {
              "$ref": "#/definitions/Level"
            }
          ]
        },
        "fstring-type-annotation": {
````







**Tool Use: find_matching_chunks_in_file**

````json
{
  "filter_": "[\"\"]",
  "rel_path": "crates/red_knot/src/args.rs",
  "project_name": "ruff_project"
}
````

**Tool Result: find_matching_chunks_in_file**

````
(1 of 1 chunks)
id=whole_file_b14cacd37b (category=whole_file chars=8553)
````







**Tool Use: chunk_details**

````json
{
  "chunk_id": "whole_file_b14cacd37b"
}
````

**Tool Result: chunk_details**

````
use crate::logging::Verbosity;
use crate::python_version::PythonVersion;
use clap::{ArgAction, ArgMatches, Error, Parser};
use red_knot_project::metadata::options::{EnvironmentOptions, Options, TerminalOptions};
use red_knot_project::metadata::value::{RangedValue, RelativePathBuf};
use red_knot_python_semantic::lint;
use ruff_db::system::SystemPathBuf;

#[derive(Debug, Parser)]
#[command(
    author,
    name = "red-knot",
    about = "An extremely fast Python type checker."
)]
#[command(version)]
pub(crate) struct Args {
    #[command(subcommand)]
    pub(crate) command: Command,
}

#[derive(Debug, clap::Subcommand)]
pub(crate) enum Command {
    /// Check a project for type errors.
    Check(CheckCommand),

    /// Start the language server
    Server,

    /// Display Red Knot's version
    Version,
}

#[derive(Debug, Parser)]
pub(crate) struct CheckCommand {
    /// List of files or directories to check.
    #[clap(
        help = "List of files or directories to check [default: the project root]",
        value_name = "PATH"
    )]
    pub paths: Vec<SystemPathBuf>,

    /// Run the command within the given project directory.
    ///
    /// All `pyproject.toml` files will be discovered by walking up the directory tree from the given project directory,
    /// as will the project's virtual environment (`.venv`) unless the `venv-path` option is set.
    ///
    /// Other command-line arguments (such as relative paths) will be resolved relative to the current working directory.
    #[arg(long, value_name = "PROJECT")]
    pub(crate) project: Option<SystemPathBuf>,

    /// Path to the Python installation from which Red Knot resolves type information and third-party dependencies.
    ///
    /// Red Knot will search in the path's `site-packages` directories for type information and
    /// third-party imports.
    ///
    /// This option is commonly used to specify the path to a virtual environment.
    #[arg(long, value_name = "PATH")]
    pub(crate) python: Option<SystemPathBuf>,

    /// Custom directory to use for stdlib typeshed stubs.
    #[arg(long, value_name = "PATH", alias = "custom-typeshed-dir")]
    pub(crate) typeshed: Option<SystemPathBuf>,

    /// Additional path to use as a module-resolution source (can be passed multiple times).
    #[arg(long, value_name = "PATH")]
    pub(crate) extra_search_path: Option<Vec<SystemPathBuf>>,

    /// Python version to assume when resolving types.
    #[arg(long, value_name = "VERSION", alias = "target-version")]
    pub(crate) python_version: Option<PythonVersion>,

    #[clap(flatten)]
    pub(crate) verbosity: Verbosity,

    #[clap(flatten)]
    pub(crate) rules: RulesArg,

    /// The format to use for printing diagnostic messages.
    #[arg(long)]
    pub(crate) output_format: Option<OutputFormat>,

    /// Use exit code 1 if there are any warning-level diagnostics.
    #[arg(long, conflicts_with = "exit_zero", default_missing_value = "true", num_args=0..1)]
    pub(crate) error_on_warning: Option<bool>,

    /// Always use exit code 0, even when there are error-level diagnostics.
    #[arg(long)]
    pub(crate) exit_zero: bool,

    /// Watch files for changes and recheck files related to the changed files.
    #[arg(long, short = 'W')]
    pub(crate) watch: bool,
}

impl CheckCommand {
    pub(crate) fn into_options(self) -> Options {
        let rules = if self.rules.is_empty() {
            None
        } else {
            Some(
                self.rules
                    .into_iter()
                    .map(|(rule, level)| (RangedValue::cli(rule), RangedValue::cli(level)))
                    .collect(),
            )
        };

        Options {
            environment: Some(EnvironmentOptions {
                python_version: self
                    .python_version
                    .map(|version| RangedValue::cli(version.into())),
                python: self.python.map(RelativePathBuf::cli),
                typeshed: self.typeshed.map(RelativePathBuf::cli),
                extra_paths: self.extra_search_path.map(|extra_search_paths| {
                    extra_search_paths
                        .into_iter()
                        .map(RelativePathBuf::cli)
                        .collect()
                }),
                ..EnvironmentOptions::default()
            }),
            terminal: Some(TerminalOptions {
                output_format: self
                    .output_format
                    .map(|output_format| RangedValue::cli(output_format.into())),
                error_on_warning: self.error_on_warning,
            }),
            rules,
            ..Default::default()
        }
    }
}

/// A list of rules to enable or disable with a given severity.
///
/// This type is used to parse the `--error`, `--warn`, and `--ignore` arguments
/// while preserving the order in which they were specified (arguments last override previous severities).
#[derive(Debug)]
pub(crate) struct RulesArg(Vec<(String, lint::Level)>);

impl RulesArg {
    fn is_empty(&self) -> bool {
        self.0.is_empty()
    }

    fn into_iter(self) -> impl Iterator<Item = (String, lint::Level)> {
        self.0.into_iter()
    }
}

impl clap::FromArgMatches for RulesArg {
    fn from_arg_matches(matches: &ArgMatches) -> Result<Self, Error> {
        let mut rules = Vec::new();

        for (level, arg_id) in [
            (lint::Level::Ignore, "ignore"),
            (lint::Level::Warn, "warn"),
            (lint::Level::Error, "error"),
        ] {
            let indices = matches.indices_of(arg_id).into_iter().flatten();
            let levels = matches.get_many::<String>(arg_id).into_iter().flatten();
            rules.extend(
                indices
                    .zip(levels)
                    .map(|(index, rule)| (index, rule, level)),
            );
        }

        // Sort by their index so that values specified later override earlier ones.
        rules.sort_by_key(|(index, _, _)| *index);

        Ok(Self(
            rules
                .into_iter()
                .map(|(_, rule, level)| (rule.to_owned(), level))
                .collect(),
        ))
    }

    fn update_from_arg_matches(&mut self, matches: &ArgMatches) -> Result<(), Error> {
        self.0 = Self::from_arg_matches(matches)?.0;
        Ok(())
    }
}

impl clap::Args for RulesArg {
    fn augment_args(cmd: clap::Command) -> clap::Command {
        const HELP_HEADING: &str = "Enabling / disabling rules";

        cmd.arg(
            clap::Arg::new("error")
                .long("error")
                .action(ArgAction::Append)
                .help("Treat the given rule as having severity 'error'. Can be specified multiple times.")
                .value_name("RULE")
                .help_heading(HELP_HEADING),
        )
        .arg(
            clap::Arg::new("warn")
                .long("warn")
                .action(ArgAction::Append)
                .help("Treat the given rule as having severity 'warn'. Can be specified multiple times.")
                .value_name("RULE")
                .help_heading(HELP_HEADING),
        )
        .arg(
            clap::Arg::new("ignore")
                .long("ignore")
                .action(ArgAction::Append)
                .help("Disables the rule. Can be specified multiple times.")
                .value_name("RULE")
                .help_heading(HELP_HEADING),
        )
    }

    fn augment_args_for_update(cmd: clap::Command) -> clap::Command {
        Self::augment_args(cmd)
    }
}

/// The diagnostic output format.
#[derive(Copy, Clone, Hash, Debug, PartialEq, Eq, PartialOrd, Ord, Default, clap::ValueEnum)]
pub enum OutputFormat {
    /// Print diagnostics verbosely, with context and helpful hints.
    ///
    /// Diagnostic messages may include additional context and
    /// annotations on the input to help understand the message.
    #[default]
    #[value(name = "full")]
    Full,
    /// Print diagnostics concisely, one per line.
    ///
    /// This will guarantee that each diagnostic is printed on
    /// a single line. Only the most important or primary aspects
    /// of the diagnostic are included. Contextual information is
    /// dropped.
    #[value(name = "concise")]
    Concise,
}

impl From<OutputFormat> for ruff_db::diagnostic::DiagnosticFormat {
    fn from(format: OutputFormat) -> ruff_db::diagnostic::DiagnosticFormat {
        match format {
            OutputFormat::Full => Self::Full,
            OutputFormat::Concise => Self::Concise,
        }
    }
}
````








Now let's check the docs in the crates/red_knot/docs directory:

**Tool Use: find_matching_chunks_in_file**

````json
{
  "filter_": "[\"\"]",
  "rel_path": "crates/red_knot/docs/mypy_primer.md",
  "project_name": "ruff_project"
}
````

**Tool Result: find_matching_chunks_in_file**

````
(5 of 5 chunks)
id=Running `mypy_primer`_27938374d9 (category=markdown section chars=24)
id=Basics_314ecf98a4 (category=markdown section chars=562)
id=Showing the diagnostics diff between two Git revisions_a34c2aea37 (category=markdown section chars=756)
id=Avoiding recompilation_b7e9feb252 (category=markdown section chars=306)
id=Running from a local copy of the repository_e875a28be8 (category=markdown section chars=726)
````








**Tool Use: chunk_details**

````json
{
  "chunk_id": "Basics_314ecf98a4"
}
````

**Tool Result: chunk_details**

````
## Basics

For now, we use our own [fork of mypy primer]. It can be run using `uvx --from "…" mypy_primer`. For example, to see the help message, run:

```sh
uvx --from "git+https://github.com/astral-sh/mypy_primer.git@add-red-knot-support" mypy_primer -h
```

Alternatively, you can install the forked version of `mypy_primer` using:

```sh
uv tool install "git+https://github.com/astral-sh/mypy_primer.git@add-red-knot-support"
```

and then run it using `uvx mypy_primer` or just `mypy_primer`, if your `PATH` is set up accordingly (see: [Tool executables]).
````









**Tool Use: chunk_details**

````json
{
  "chunk_id": "Running from a local copy of the repository_e875a28be8"
}
````

**Tool Result: chunk_details**

````
## Running from a local copy of the repository

If you are working on a local branch, you can use `mypy_primer`'s `--repo` option to specify the path to your local copy of the `ruff` repository.
This allows `mypy_primer` to check out local branches:

```sh
mypy_primer --repo /path/to/ruff --old origin/main --new my/local-branch …
```

Note that you might need to clean up `/tmp/mypy_primer` in order for this to work correctly.

[fork of mypy primer]: https://github.com/astral-sh/mypy_primer/tree/add-red-knot-support
[full list of ecosystem projects]: https://github.com/astral-sh/mypy_primer/blob/add-red-knot-support/mypy_primer/projects.py
[tool executables]: https://docs.astral.sh/uv/concepts/tools/#tool-executables
````







Let's check if there are any examples in the repo that show how to use Red Knot:

**Tool Use: find_files_by_chunk_content**

````json
{
  "project_name": "ruff_project",
  "chunk_contents_filter": "[\"red knot example\", \"knot example\", \"how to use red knot\"]"
}
````

**Tool Result: find_files_by_chunk_content**

````
No files found
````







Let's look at the main.rs file in the red_knot crate:

**Tool Use: find_matching_chunks_in_file**

````json
{
  "filter_": "[\"\"]",
  "rel_path": "crates/red_knot/src/main.rs",
  "project_name": "ruff_project"
}
````

**Tool Result: find_matching_chunks_in_file**

````
(2 of 2 chunks)
id=whole_file_part1_0eb4b07d44 (category=whole_file chars=9974)
id=whole_file_part2_a6df340756 (category=whole_file chars=2773)
````









**Tool Use: chunk_details**

````json
{
  "chunk_id": "whole_file_part1_0eb4b07d44"
}
````

**Tool Result: chunk_details**

````
[This is a subsection of the chunk. Other parts contain the rest of the chunk]

use std::io::{self, stdout, BufWriter, Write};
use std::process::{ExitCode, Termination};

use anyhow::Result;
use std::sync::Mutex;

use crate::args::{Args, CheckCommand, Command};
use crate::logging::setup_tracing;
use anyhow::{anyhow, Context};
use clap::Parser;
use colored::Colorize;
use crossbeam::channel as crossbeam_channel;
use red_knot_project::metadata::options::Options;
use red_knot_project::watch::ProjectWatcher;
use red_knot_project::{watch, Db};
use red_knot_project::{ProjectDatabase, ProjectMetadata};
use red_knot_server::run_server;
use ruff_db::diagnostic::{DisplayDiagnosticConfig, OldDiagnosticTrait, Severity};
use ruff_db::system::{OsSystem, SystemPath, SystemPathBuf};
use salsa::plumbing::ZalsaDatabase;

mod args;
mod logging;
mod python_version;
mod version;

#[allow(clippy::print_stdout, clippy::unnecessary_wraps, clippy::print_stderr)]
pub fn main() -> ExitStatus {
    run().unwrap_or_else(|error| {
        use std::io::Write;

        // Use `writeln` instead of `eprintln` to avoid panicking when the stderr pipe is broken.
        let mut stderr = std::io::stderr().lock();

        // This communicates that this isn't a linter error but Red Knot itself hard-errored for
        // some reason (e.g. failed to resolve the configuration)
        writeln!(stderr, "{}", "Red Knot failed".red().bold()).ok();
        // Currently we generally only see one error, but e.g. with io errors when resolving
        // the configuration it is help to chain errors ("resolving configuration failed" ->
        // "failed to read file: subdir/pyproject.toml")
        for cause in error.chain() {
            // Exit "gracefully" on broken pipe errors.
            //
            // See: https://github.com/BurntSushi/ripgrep/blob/bf63fe8f258afc09bae6caa48f0ae35eaf115005/crates/core/main.rs#L47C1-L61C14
            if let Some(ioerr) = cause.downcast_ref::<io::Error>() {
                if ioerr.kind() == io::ErrorKind::BrokenPipe {
                    return ExitStatus::Success;
                }
            }

            writeln!(stderr, "  {} {cause}", "Cause:".bold()).ok();
        }

        ExitStatus::Error
    })
}

fn run() -> anyhow::Result<ExitStatus> {
    let args = wild::args_os();
    let args = argfile::expand_args_from(args, argfile::parse_fromfile, argfile::PREFIX)
        .context("Failed to read CLI arguments from file")?;
    let args = Args::parse_from(args);

    match args.command {
        Command::Server => run_server().map(|()| ExitStatus::Success),
        Command::Check(check_args) => run_check(check_args),
        Command::Version => version().map(|()| ExitStatus::Success),
    }
}

pub(crate) fn version() -> Result<()> {
    let mut stdout = BufWriter::new(io::stdout().lock());
    let version_info = crate::version::version();
    writeln!(stdout, "red knot {}", &version_info)?;
    Ok(())
}

fn run_check(args: CheckCommand) -> anyhow::Result<ExitStatus> {
    let verbosity = args.verbosity.level();
    countme::enable(verbosity.is_trace());
    let _guard = setup_tracing(verbosity)?;

    tracing::debug!("Version: {}", version::version());

    // The base path to which all CLI arguments are relative to.
    let cwd = {
        let cwd = std::env::current_dir().context("Failed to get the current working directory")?;
        SystemPathBuf::from_path_buf(cwd)
            .map_err(|path| {
                anyhow!(
                    "The current working directory `{}` contains non-Unicode characters. Red Knot only supports Unicode paths.",
                    path.display()
                )
            })?
    };

    let project_path = args
        .project
        .as_ref()
        .map(|project| {
            if project.as_std_path().is_dir() {
                Ok(SystemPath::absolute(project, &cwd))
            } else {
                Err(anyhow!(
                    "Provided project path `{project}` is not a directory"
                ))
            }
        })
        .transpose()?
        .unwrap_or_else(|| cwd.clone());

    let check_paths: Vec<_> = args
        .paths
        .iter()
        .map(|path| SystemPath::absolute(path, &cwd))
        .collect();

    let system = OsSystem::new(cwd);
    let watch = args.watch;
    let exit_zero = args.exit_zero;

    let cli_options = args.into_options();
    let mut project_metadata = ProjectMetadata::discover(&project_path, &system)?;
    project_metadata.apply_cli_options(cli_options.clone());
    project_metadata.apply_configuration_files(&system)?;

    let mut db = ProjectDatabase::new(project_metadata, system)?;

    if !check_paths.is_empty() {
        db.project().set_included_paths(&mut db, check_paths);
    }

    let (main_loop, main_loop_cancellation_token) = MainLoop::new(cli_options);

    // Listen to Ctrl+C and abort the watch mode.
    let main_loop_cancellation_token = Mutex::new(Some(main_loop_cancellation_token));
    ctrlc::set_handler(move || {
        let mut lock = main_loop_cancellation_token.lock().unwrap();

        if let Some(token) = lock.take() {
            token.stop();
        }
    })?;

    let exit_status = if watch {
        main_loop.watch(&mut db)?
    } else {
        main_loop.run(&mut db)?
    };

    tracing::trace!("Counts for entire CLI run:\n{}", countme::get_all());

    std::mem::forget(db);

    if exit_zero {
        Ok(ExitStatus::Success)
    } else {
        Ok(exit_status)
    }
}

#[derive(Copy, Clone)]
pub enum ExitStatus {
    /// Checking was successful and there were no errors.
    Success = 0,

    /// Checking was successful but there were errors.
    Failure = 1,

    /// Checking failed.
    Error = 2,
}

impl Termination for ExitStatus {
    fn report(self) -> ExitCode {
        ExitCode::from(self as u8)
    }
}

struct MainLoop {
    /// Sender that can be used to send messages to the main loop.
    sender: crossbeam_channel::Sender<MainLoopMessage>,

    /// Receiver for the messages sent **to** the main loop.
    receiver: crossbeam_channel::Receiver<MainLoopMessage>,

    /// The file system watcher, if running in watch mode.
    watcher: Option<ProjectWatcher>,

    cli_options: Options,
}

impl MainLoop {
    fn new(cli_options: Options) -> (Self, MainLoopCancellationToken) {
        let (sender, receiver) = crossbeam_channel::bounded(10);

        (
            Self {
                sender: sender.clone(),
                receiver,
                watcher: None,
                cli_options,
            },
            MainLoopCancellationToken { sender },
        )
    }

    fn watch(mut self, db: &mut ProjectDatabase) -> Result<ExitStatus> {
        tracing::debug!("Starting watch mode");
        let sender = self.sender.clone();
        let watcher = watch::directory_watcher(move |event| {
            sender.send(MainLoopMessage::ApplyChanges(event)).unwrap();
        })?;

        self.watcher = Some(ProjectWatcher::new(watcher, db));

        self.run(db)?;

        Ok(ExitStatus::Success)
    }

    fn run(mut self, db: &mut ProjectDatabase) -> Result<ExitStatus> {
        self.sender.send(MainLoopMessage::CheckWorkspace).unwrap();

        let result = self.main_loop(db);

        tracing::debug!("Exiting main loop");

        result
    }

    fn main_loop(&mut self, db: &mut ProjectDatabase) -> Result<ExitStatus> {
        // Schedule the first check.
        tracing::debug!("Starting main loop");

        let mut revision = 0u64;

        while let Ok(message) = self.receiver.recv() {
            match message {
                MainLoopMessage::CheckWorkspace => {
                    let db = db.clone();
                    let sender = self.sender.clone();

                    // Spawn a new task that checks the project. This needs to be done in a separate thread
                    // to prevent blocking the main loop here.
                    rayon::spawn(move || {
                        if let Ok(result) = db.check() {
                            // Send the result back to the main loop for printing.
                            sender
                                .send(MainLoopMessage::CheckCompleted { result, revision })
                                .unwrap();
                        }
                    });
                }

                MainLoopMessage::CheckCompleted {
                    result,
                    revision: check_revision,
                } => {
                    let display_config = DisplayDiagnosticConfig::default()
                        .format(db.project().settings(db).terminal().output_format)
                        .color(colored::control::SHOULD_COLORIZE.should_colorize());

                    let min_error_severity =
                        if db.project().settings(db).terminal().error_on_warning {
                            Severity::Warning
                        } else {
                            Severity::Error
                        };

                    if check_revision == revision {
                        if db.project().files(db).is_empty() {
                            tracing::warn!("No python files found under the given path(s)");
                        }

                        let mut stdout = stdout().lock();

                        if result.is_empty() {
                            writeln!(stdout, "All checks passed!")?;

                            if self.watcher.is_none() {
                                return Ok(ExitStatus::Success);
                            }
                        } else {
                            let mut failed = false;
                            let diagnostics_count = result.len();

                            for diagnostic in result {
                                writeln!(stdout, "{}", diagnostic.display(db, &display_config))?;

                                failed |= diagnostic.severity() >= min_error_severity;
````










**Tool Use: chunk_details**

````json
{
  "chunk_id": "whole_file_part2_a6df340756"
}
````

**Tool Result: chunk_details**

````
[This is a subsection of the chunk. Other parts contain the rest of the chunk]

                            }

                            writeln!(
                                stdout,
                                "Found {} diagnostic{}",
                                diagnostics_count,
                                if diagnostics_count > 1 { "s" } else { "" }
                            )?;

                            if self.watcher.is_none() {
                                return Ok(if failed {
                                    ExitStatus::Failure
                                } else {
                                    ExitStatus::Success
                                });
                            }
                        }
                    } else {
                        tracing::debug!(
                            "Discarding check result for outdated revision: current: {revision}, result revision: {check_revision}"
                        );
                    }

                    tracing::trace!("Counts after last check:\n{}", countme::get_all());
                }

                MainLoopMessage::ApplyChanges(changes) => {
                    revision += 1;
                    // Automatically cancels any pending queries and waits for them to complete.
                    db.apply_changes(changes, Some(&self.cli_options));
                    if let Some(watcher) = self.watcher.as_mut() {
                        watcher.update(db);
                    }
                    self.sender.send(MainLoopMessage::CheckWorkspace).unwrap();
                }
                MainLoopMessage::Exit => {
                    // Cancel any pending queries and wait for them to complete.
                    // TODO: Don't use Salsa internal APIs
                    //  [Zulip-Thread](https://salsa.zulipchat.com/#narrow/stream/333573-salsa-3.2E0/topic/Expose.20an.20API.20to.20cancel.20other.20queries)
                    let _ = db.zalsa_mut();
                    return Ok(ExitStatus::Success);
                }
            }

            tracing::debug!("Waiting for next main loop message.");
        }

        Ok(ExitStatus::Success)
    }
}

#[derive(Debug)]
struct MainLoopCancellationToken {
    sender: crossbeam_channel::Sender<MainLoopMessage>,
}

impl MainLoopCancellationToken {
    fn stop(self) {
        self.sender.send(MainLoopMessage::Exit).unwrap();
    }
}

/// Message sent from the orchestrator to the main loop.
#[derive(Debug)]
enum MainLoopMessage {
    CheckWorkspace,
    CheckCompleted {
        /// The diagnostics that were found during the check.
        result: Vec<Box<dyn OldDiagnosticTrait>>,
        revision: u64,
    },
    ApplyChanges(Vec<watch::ChangeEvent>),
    Exit,
}
````







Let's check the benchmark directory to see if there are examples of Red Knot usage there:

**Tool Use: find_matching_chunks_in_file**

````json
{
  "filter_": "[\"\"]",
  "rel_path": "scripts/knot_benchmark/README.md",
  "project_name": "ruff_project"
}
````

**Tool Result: find_matching_chunks_in_file**

````
(3 of 3 chunks)
id=Getting started_f5e8407982 (category=markdown section chars=389)
id=Known limitations_35bd18c251 (category=markdown section chars=260)
id=Windows support_1cedc0e6e9 (category=markdown section chars=169)
````










**Tool Use: chunk_details**

````json
{
  "chunk_id": "Getting started_f5e8407982"
}
````

**Tool Result: chunk_details**

````
## Getting started

1. [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/)

- Unix: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

1. Build red_knot: `cargo build --bin red_knot --release`
1. `cd` into the benchmark directory: `cd scripts/knot_benchmark`
1. Run benchmarks: `uv run benchmark`
````












Let's check the most recently checked out branches and see if they provide any information on the status of red knot development:

**Tool Use: list_most_recently_checked_out_branches**

````json
{
  "n": 20,
  "project_name": "ruff_project"
}
````

**Tool Result: list_most_recently_checked_out_branches**

````

````












Let's look at the red_knot_test README, which might have more information:

**Tool Use: find_matching_chunks_in_file**

````json
{
  "filter_": "[\"\"]",
  "rel_path": "crates/red_knot_test/README.md",
  "project_name": "ruff_project"
}
````

**Tool Result: find_matching_chunks_in_file**

````
(37 of 37 chunks)
id=Writing type-checking / type-inference tests_5709c05eef (category=markdown section chars=2583)
id=Assertions_4c1f3d8b31 (category=markdown section chars=98)
id=Assertion kinds_ab1f62533f (category=markdown section chars=20)
id=revealed_3db49675b2 (category=markdown section chars=1236)
id=error_a555b297d8 (category=markdown section chars=1286)
id=Assertion locations_c5ac99f75c (category=markdown section chars=311)
id=error: [invalid-assignment]_2aea864428 (category=markdown section chars=114)
id=error: [invalid-assignment]_5d49208e57 (category=markdown section chars=29)
id=revealed: Literal[1]_36a860f1db (category=markdown section chars=332)
id=Literate style_e7a256fa62 (category=markdown section chars=271)
id=My literate test_ee1af93376 (category=markdown section chars=243)
id=Diagnostic Snapshotting_7f1528e332 (category=markdown section chars=245)
id=Unresolvable module import_802d91ed03 (category=markdown section chars=570)
id=Multi-file tests_c9a8a7c304 (category=markdown section chars=814)
id=Multi-test suites_75f451326b (category=markdown section chars=148)
id=Same-file invalid assignment_488b3127f3 (category=markdown section chars=88)
id=Cross-file invalid assignment_d15c75cf4a (category=markdown section chars=1040)
id=Structured test suites_fa5e7df9cb (category=markdown section chars=113)
id=Literals_0bd1d5248f (category=markdown section chars=11)
id=Numbers_f80bc22c11 (category=markdown section chars=11)
id=Integer_c402b64727 (category=markdown section chars=62)
id=Float_a7bd4e267d (category=markdown section chars=57)
id=Strings_1051c6b872 (category=markdown section chars=477)
id=Configuration_a61b973413 (category=markdown section chars=646)
id=Specifying a custom typeshed_22290a351e (category=markdown section chars=322)
id=Documentation of tests_d99ddd0640 (category=markdown section chars=410)
id=Running the tests_98a64deed1 (category=markdown section chars=518)
id=Planned features_586c4c6620 (category=markdown section chars=131)
id=Multi-line diagnostic assertions_97f104b8e0 (category=markdown section chars=548)
id=Configuring search paths and kinds_e811c7f1b0 (category=markdown section chars=1072)
id=I/O errors_429b072992 (category=markdown section chars=133)
id=Asserting on full diagnostic output_301b68fa3e (category=markdown section chars=873)
id=full output_10f4786511 (category=markdown section chars=848)
id=Incremental tests_abae2a03c7 (category=markdown section chars=324)
id=Incremental_909e86bd05 (category=markdown section chars=14)
id=modify a file_fd2ed40b93 (category=markdown section chars=331)
id=b.py_4f0ac13910 (category=markdown section chars=1593)
````











Based on my research, I can now provide instructions on how to set up and run the Red Knot type checker.

**Tool Use: artifacts**

````json
{
  "id": "red-knot-setup",
  "type": "application/vnd.ant.code",
  "title": "Setting up Red Knot Type Checker",
  "command": "create",
  "content": "# Setting up the Red Knot Type Checker\n\nRed Knot is an extremely fast Python type checker developed by the Ruff team. It's designed to prioritize good type inference even in unannotated code and aims to avoid false positives. It's currently under active development and is not yet officially released, but you can try it out from the source.\n\n## Prerequisites\n\n- Rust toolchain installed (https://rustup.rs/)\n- Git\n\n## Step 1: Clone the Ruff repository\n\n```bash\ngit clone https://github.com/astral-sh/ruff.git\ncd ruff\n```\n\n## Step 2: Build Red Knot\n\n```bash\ncargo build --bin red_knot --release\n```\n\nThis will produce a binary at `target/release/red_knot`.\n\n## Step 3: Basic Usage\n\nThe Red Knot binary provides a `check` command that works similar to tools like mypy:\n\n```bash\n# Check files or directories (from project root)\n./target/release/red_knot check path/to/your/python/files\n\n# Check with python version specified\n./target/release/red_knot check --python-version 3.11 path/to/your/python/files\n\n# Set severity levels for specific rules\n./target/release/red_knot check --error call-non-callable --warn call-possibly-unbound-method path/to/your/python/files\n\n# Watch mode (automatically rechecks when files change)\n./target/release/red_knot check --watch path/to/your/python/files\n```\n\n## Step 4: Configuration\n\nRed Knot can be configured in your project's `pyproject.toml` file. Here's an example configuration:\n\n```toml\n[tool.knot]\n# Environment settings\nenvironment.python-version = \"3.11\"  # Target Python version\nenvironment.python = \".venv\"  # Path to Python environment (for third-party imports)\nenvironment.extra-paths = [\"path/to/extra/modules\"]  # Additional module search paths\n\n# Terminal settings\nterminal.output-format = \"full\"  # \"full\" or \"concise\"\nterminal.error-on-warning = true  # Exit with error code on warnings\n\n# Configure rule severities\nrules.call-non-callable = \"error\"\nrules.call-possibly-unbound-method = \"warn\"\n```\n\n## Migrating from mypy to Red Knot\n\nSince Red Knot is still in development, migrating from mypy should be done with caution:\n\n1. **Run both in parallel**: Keep mypy running while you test Red Knot on your codebase\n2. **Configure Python version**: Make sure to set the same Python version as in your mypy config\n3. **Environment setup**: Configure virtual environments correctly to ensure third-party imports work\n4. **Analyze differences**: Red Knot may produce different results than mypy as noted in its README (by design)\n\n### Comparing Red Knot with mypy\n\nFor a side-by-side comparison of mypy and Red Knot on your codebase, you can use the mypy_primer tool (forked by the Ruff team):\n\n```bash\n# Install mypy_primer\nuv tool install \"git+https://github.com/astral-sh/mypy_primer.git@add-red-knot-support\"\n\n# Run comparison\nmypy_primer --repo /path/to/ruff --old-tool mypy --new-tool red-knot\n```\n\n## Limitations\n\n- Red Knot is still under development and may not support all mypy features\n- Documentation is limited as the project is not officially released\n- The API and CLI interface may change in future versions\n",
  "language": "markdown",
  "version_uuid": "1c12d436-b220-4ae4-b3af-70d75d8a44c7"
}
````

**Tool Result: artifacts**

````
OK
````



Based on my investigation into the Ruff codebase, I've put together instructions for setting up and using the Red Knot type checker.

Red Knot is clearly a type checker being developed by the Ruff team, written in Rust. It's currently under development and not officially released for general use yet - the README itself mentions "it is a work-in-progress and not ready for user testing."

Here's what I've discovered:

1. Red Knot is built as a binary using Cargo
2. It supports a CLI interface with commands like `check` and `server`
3. Configuration can be done through:
   - `pyproject.toml` file
   - Command-line arguments 
   - A dedicated configuration file (uses the schema defined in knot.schema.json)

The most straightforward way to try Red Knot would be to build it from source and run it on your Python code.

The configuration options are similar to other type checkers - you can specify Python version, environment paths, and rule severities. The command-line interface is also familiar, allowing you to check files/directories and set rule severities.

For detailed setup and usage instructions, please refer to the document I've created. Note that since the tool is still in development, the interface and features may change over time.

Would you like me to explore any specific aspect of Red Knot in more detail?



