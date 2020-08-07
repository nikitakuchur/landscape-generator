# Landscape generator
Two neural networks implemented in PyTorch for heighmap generation.
You can read an article about this project [here](https://github.com/nikitakuchur/landscape-generator/blob/master/article/heightmap-generation-with-neural-networks.pdf) (RUS).

Note, that I'm not a Python developer and I have no experience with neural networks. Please, let me know if you find any strange things in this code that I should fix. Thank you.

In the following sections, you can see some interesting results that I accomplished in this little project.


## Variational Autoencoder

### Reconstruction

![VAE reconstruction](https://github.com/nikitakuchur/landscape-generator/blob/master/images/vae-reconstruction.png)

### Generation

![VAE generation](https://github.com/nikitakuchur/landscape-generator/blob/master/images/vae-generation.png)

### Interpolation

![VAE interpolation](https://github.com/nikitakuchur/landscape-generator/blob/master/images/vae-interpolation.png)

### Terrains

![VAE terrains](https://github.com/nikitakuchur/landscape-generator/blob/master/images/vae-3d.png)


## Generative adversarial network

### Generation

![GAN generation](https://github.com/nikitakuchur/landscape-generator/blob/master/images/gan-generation.png)

### Interpolation

![GAN interpolation](https://github.com/nikitakuchur/landscape-generator/blob/master/images/gan-interpolation.png)

### Terrains

![GAN terrains](https://github.com/nikitakuchur/landscape-generator/blob/master/images/gan-3d.png)
