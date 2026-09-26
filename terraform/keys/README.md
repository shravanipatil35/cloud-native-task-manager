Place the public key matching your AWS EC2 key pair here as `<key-name>.pub`, using the `ec2_key_pair_name` Terraform value.

To derive the public key from an existing private key:

```sh
ssh-keygen -y -f <private-key-file> > <key-name>.pub
```

Keep the private key outside the repository. Private key files are ignored by Git.
