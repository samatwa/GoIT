# Airflow sandbox

## Clone and authenticate

The upstream exercise originated in `goitacademy/airflow_sandbox`. This copy is maintained within the GoIT collection. Clone the collection and work in this project directory:

```bash
git clone https://github.com/samatwa/GoIT.git
cd GoIT/DataEngineering/airflow_sandbox
```

Use Git Credential Manager or another configured Git credential helper for authenticated pushes. Keep access tokens out of remote URLs and committed files.

## Encrypt files

Place the input file in the project working directory, then use the included public key:

```bash
./encrypt_and_archive.sh file_name public_key.pem
```

On PowerShell:

```powershell
.\encrypt_and_archive.ps1 -InputFile "path_to_file" -PublicKey "path_to_public_key.pem"
```

Here `file_name` is the input file and `public_key.pem` is the provided public key. Move the resulting encrypted archive into `encrypted_file/`. The original exercise used this example archive name:

```bash
mv file_name_tar.gz encrypted_file/
```

## Commit changes

From the project directory:

```bash
git add encrypted_file/
git commit -m "Encrypt files and add the archive"
git push
```

The nested historical workflow is retained as course material. GitHub does not run workflows from this nested directory automatically.

## Resolve conflicts

Pull the current collection branch before editing:

```bash
git pull origin main
```

If a file has conflict markers, reconcile the two versions:

```text
<<<<<<< HEAD
Your changes
=======
Remote changes
>>>>>>> commit_id
```

Remove the markers after keeping the correct content, then stage and commit:

```bash
git add <file_name>
git commit -m "Resolve conflicts"
git push
```

Verify the resulting commit and files on GitHub.
