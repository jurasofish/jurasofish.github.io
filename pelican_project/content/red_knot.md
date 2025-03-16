Title: A Very (!) Early Play With Astral's Red Knot Static Type Checker
Date: 2025-03-16 11:30

_This is a casual look at a WIP piece of software that I know nothing about - don't draw too many conclusions from this._

[Astral](https://astral.sh/) is doing The Lord's work with python tooling.
[Ruff](https://github.com/astral-sh/ruff) is a joy to use for both formatting and linting. 
And the newer [uv](https://github.com/astral-sh/uv) has breathed fresh
air into environment management, 
[solving the Python bootstrapping problem](https://www.bitecode.dev/p/a-year-of-uv-pros-cons-and-should?open=false#%C2%A7bootstrapping-done-right)
(I'm calling it) and generally becoming a community go-to tool overnight.
These tools have improved my day to day dev experience massively.

The most annoying (slow) part of my dev experience is now mypy. And oh boy,
[Astral is coming for it](https://x.com/charliermarsh/status/1846544708480168229)
with a project called _Red Knot_ (actually I don't know that's its name but it seems
to be the working name for the moment).

It was [recently announced](https://bsky.app/profile/crmarsh.com/post/3lgvhzdfrps26) 
that Red Knot is under development (explicitly ["this project is _not_ ready for real-world user testing"](https://bsky.app/profile/crmarsh.com/post/3lgvhzeie6226) - sorry!).
You can see a [flurry of activity on github](https://github.com/astral-sh/ruff/pulls?q=is%3Apr+label%3Ared-knot+).
And it's worth noting that ["red knot will certainly not be a drop-in replacement for either mypy or pyright"](https://github.com/astral-sh/ruff/discussions/15149#discussioncomment-11670666).

Well I can't wait and I just want to get my mitts on it today.
Welcome to my blog post where I have a go at getting it up and running.

## Compiling

Red knot hasn't been released, there are no docs I can see, nor any binaries.
Looks like I'll have to dig into the ruff codebase to figure out how to build & run it.
I know nothing about the ruff codebase. Except that it's largely written in rust.
And I don't know a lick of rust. These days that's no problem, you can just
get AI to figure things out for you, right? We'll find out.

I've cloned the ruff repo 
([commit](https://github.com/astral-sh/ruff/commit/2de8455e43efc55b2ed302c0bdf4e59744338504)) 
and thrown the problem to [MCPunk](https://github.com/jurasofish/mcpunk)
via Claude Desktop with Claude Sonnet 3.7 and the prompt:

> Hey buddy can you set up the ~/git/ruff project and show me how to run the red knot type checker. Notably it's still under development, with no published docs I am aware of, so you'll likely need to dig into CI or find documentation that may be written but not yet published (perhaps this is in docstrings, perhaps it doesn't exist).
>
>Ultimately I would like instructions on how to switch from mypy to red knot, so that I can do an early assessment of red knot. You don't need to provide that straight away, just start simple and we'll work towards it together.
>
>Thank you!

Note I have some stuff about MCPunk in my preferences included in every chat, so you
might need to tell it a bit more explicitly to use MCPunk.
Claude dutifully beavered away for a couple of minutes, making about 25 tool uses
explore the project, and spat out the following.
[Full conversation here]({filename}/red_knot_conversation.md) if you're curious
to see what it looked at as it produced this.

````markdown
# Setting up the Red Knot Type Checker

Red Knot is an extremely fast Python type checker developed by the Ruff team. It's designed to prioritize good type inference even in unannotated code and aims to avoid false positives. It's currently under active development and is not yet officially released, but you can try it out from the source.

## Prerequisites

- Rust toolchain installed (https://rustup.rs/)
- Git

## Step 1: Clone the Ruff repository

```bash
git clone https://github.com/astral-sh/ruff.git
cd ruff
```

## Step 2: Build Red Knot

```bash
cargo build --bin red_knot --release
```

This will produce a binary at `target/release/red_knot`.

## Step 3: Basic Usage

The Red Knot binary provides a `check` command that works similar to tools like mypy:

```bash
# Check files or directories (from project root)
./target/release/red_knot check path/to/your/python/files

# Check with python version specified
./target/release/red_knot check --python-version 3.11 path/to/your/python/files

# Set severity levels for specific rules
./target/release/red_knot check --error call-non-callable --warn call-possibly-unbound-method path/to/your/python/files

# Watch mode (automatically rechecks when files change)
./target/release/red_knot check --watch path/to/your/python/files
```

## Step 4: Configuration

Red Knot can be configured in your project's `pyproject.toml` file. Here's an example configuration:

```toml
[tool.knot]
# Environment settings
environment.python-version = "3.11"  # Target Python version
environment.python = ".venv"  # Path to Python environment (for third-party imports)
environment.extra-paths = ["path/to/extra/modules"]  # Additional module search paths

# Terminal settings
terminal.output-format = "full"  # "full" or "concise"
terminal.error-on-warning = true  # Exit with error code on warnings

# Configure rule severities
rules.call-non-callable = "error"
rules.call-possibly-unbound-method = "warn"
```

## Migrating from mypy to Red Knot

Since Red Knot is still in development, migrating from mypy should be done with caution:

1. **Run both in parallel**: Keep mypy running while you test Red Knot on your codebase
2. **Configure Python version**: Make sure to set the same Python version as in your mypy config
3. **Environment setup**: Configure virtual environments correctly to ensure third-party imports work
4. **Analyze differences**: Red Knot may produce different results than mypy as noted in its README (by design)

### Comparing Red Knot with mypy

For a side-by-side comparison of mypy and Red Knot on your codebase, you can use the mypy_primer tool (forked by the Ruff team):

```bash
# Install mypy_primer
uv tool install "git+https://github.com/astral-sh/mypy_primer.git@add-red-knot-support"

# Run comparison
mypy_primer --repo /path/to/ruff --old-tool mypy --new-tool red-knot
```

## Limitations

- Red Knot is still under development and may not support all mypy features
- Documentation is limited as the project is not officially released
- The API and CLI interface may change in future versions
````

Okay well I set up rust and ran `cargo build --bin red_knot --release`.
Compiled some stuff, a lot of green, a little yellow, no red.
Feels like it worked.

`./target/release/red_knot` looks to work:

```text
% ./target/release/red_knot
An extremely fast Python type checker.

Usage: red_knot <COMMAND>

Commands:
  check    Check a project for type errors
  server   Start the language server
  version  Display Red Knot's version
  help     Print this message or the help of the given subcommand(s)

Options:
  -h, --help     Print help
  -V, --version  Print version
```

and `./target/release/red_knot check`:

```text
Check a project for type errors

Usage: red_knot check [OPTIONS] [PATH]...

Arguments:
  [PATH]...  List of files or directories to check [default: the project root]

Options:
      --project <PROJECT>              Run the command within the given project directory
      --python <PATH>                  Path to the Python installation from which Red Knot resolves type information and third-party dependencies
      --typeshed <PATH>                Custom directory to use for stdlib typeshed stubs
      --extra-search-path <PATH>       Additional path to use as a module-resolution source (can be passed multiple times)
      --python-version <VERSION>       Python version to assume when resolving types [possible values: 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13]
  -v, --verbose...                     Use verbose output (or `-vv` and `-vvv` for more verbose output)
      --output-format <OUTPUT_FORMAT>  The format to use for printing diagnostic messages [possible values: full, concise]
      --error-on-warning               Use exit code 1 if there are any warning-level diagnostics
      --exit-zero                      Always use exit code 0, even when there are error-level diagnostics
  -W, --watch                          Watch files for changes and recheck files related to the changed files
  -h, --help                           Print help (see more with '--help')

Enabling / disabling rules:
      --error <RULE>   Treat the given rule as having severity 'error'. Can be specified multiple times.
      --warn <RULE>    Treat the given rule as having severity 'warn'. Can be specified multiple times.
      --ignore <RULE>  Disables the rule. Can be specified multiple times.
```

Let's go!

## Using

Let's start by running Red Knot on my own [MCPunk](https://github.com/jurasofish/mcpunk) codebase
(the same used above for exploring ruff code).
It's a very small codebase. Currently checked by mypy with fairly strict settings.

I copied that `./target/release/red_knot` binary into `/usr/local/bin` (mac)
for convenience.

I slapped the following at the end of `pyproject.toml`, essentially verbatim
what Claude suggested.

```toml
[tool.knot]
# Environment settings
environment.python-version = "3.11"  # Target Python version
environment.python = ".venv"  # Path to Python environment (for third-party imports)
# environment.extra-paths = ["path/to/extra/modules"]  # Additional module search paths

# Terminal settings
terminal.output-format = "full"  # "full" or "concise"
terminal.error-on-warning = true  # Exit with error code on warnings

# Configure rule severities
rules.call-non-callable = "error"
rules.call-possibly-unbound-method = "warn"
```

Then running `red_knot check .` in the MCPunk root dir, it works!
Although I do get a lot of errors.
Some odd ones like `from collections.abc import Generator` -> ``Module `collections.abc` has no member `Generator` ``
([seems to be WIP](https://github.com/astral-sh/ruff/pull/16493#discussion_r1981940638))

A slightly more interesting one where the short-circuit `or` is not picked up
as narrowing `x` from `int | None` to `int` (minimal fake example). Interestingly
only happens in a comprehension.

```text
error: lint:unsupported-operator
   --> /Users/michael/git/mcpunk/mcpunk/util.py:125:40
    |
124 | def short_me_out(x: int | None) -> bool:
125 |     _ = [z for z in [] if x is None or 1 <= x]
    |                                        ^^^^^^ Operator `<=` is not supported for types `int` and `None`, in comparing `Literal[1]` with `int | None`
126 |     return False
```

It doesn't seem to respect exhaustiveness checking with `typing.assert_never`.

Otherwise, it seems pretty solid.

I had a fiddle with `pyproject.toml`.
Fiddling `environment.python-version` to `3.7` yields additional errors
about nonexistent imports, great, as it should.
And introducing obviously wrong code changes absolutely get flagged with
useful messages.


## Yeah cool so how fast is it?

On MCPunk, `time red_knot check .` gives `red_knot check .  0.11s user 0.04s system 258% cpu 0.057 total`
so yeah pretty fast on that small codebase. And looks like it's got parallelization happening.

Let's try some larger projects. For each of these I added the above snippet
to `pyproject.toml` and set up a venv for Red Knot to look at.

Pydantic sees `red_knot check .  0.73s user 0.09s system 399% cpu 0.203 total` (with ~3k errors 😅)

Both SQLAlchemy and mypy (running Red Knot on the mypy codebase) panic 🦐 
and appear to hang with high CPU usage.

FastAPI sees `red_knot check .  0.44s user 0.18s system 403% cpu 0.153 total` (with ~1000 errors).
In comparison, mypy sees `mypy fastapi  4.38s user 0.57s system 21% cpu 22.756 total`.
That's from cold - subsequent mypy runs with no changes take about 0.2 wall seconds,
so on-par with Red Knot from cold. Making a very small change to the code and re-running
mypy takes about 0.8 wall seconds. As far as I can tell, Red Knot is not doing any caching.

## Wrap

So there you have it, I've used [MCPunk](https://github.com/jurasofish/mcpunk)
to figure out how to build, configure, and run Red Knot (please do check out
MCPunk, you may find it very useful for things like this).

And it looks to be ~100x faster than mypy from cold. But it certainly does look
to be a heavy work in progress still.

Can't wait for the formal release!

And again, please keep in mind that I started this knowing nothing about
Red Knot (and now I only know marginally more than nothing) and my analysis
may well be misrepresenting it.
Please take this post as just a casual look at it, with no concrete takeaways.
