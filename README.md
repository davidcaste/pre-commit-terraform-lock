# Git [pre-commit](http://pre-commit.com/) hook for managing Terraform lock files

A pre-commit hook for managing Terraform lock (`.terraform.lock.hcl`) files.

See also: https://github.com/pre-commit/pre-commit

## How to install

### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/davidcaste/pre-commit-terraform-lock
    rev: <VERSION> # Get the latest from: https://github.com/davidcaste/pre-commit-terraform-lock/releases
    hooks:
    -   id: check-tf-lock-file-without-zh-entries
    # -   id: ...
```

### Hooks available

#### `check-tf-lock-file-without-zh-entries`
Prevent adding a `zh:` entry to a `.terraform.lock.hcl` file.
