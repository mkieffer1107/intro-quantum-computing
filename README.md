# intro-quantum-computing

This repo stores some of the code I wrote while reading through a great quantum computing textbook by [Thomas Wong](https://www.thomaswong.net/). I ran some of it on quantum computers via the [IBM Quantum Platform](https://quantum-computing.ibm.com/).

<a href="https://www.thomaswong.net/introduction-to-classical-and-quantum-computing-1e4p.pdf"><img src="cover.jpg" alt="version 4" width="300"/></a>

## Topics Covered

### Quantum Error Correction

- **Bit-Flip Code**
  - Rotations about the x-axis (bit flip error)
  - Measure first, classical operations later: [link](https://bit.ly/3jq8EKu)
  - Controlled operations in superposition, then collapse: [link](https://bit.ly/3YXlOPF)

- **Phase-Flip Code**
  - Rotations about the z-axis (phase flip error -- change in relative phase)
  - [Link](https://bit.ly/3e7dNQR)

- **Shor Code**
  - Shor encoding with bit-flip error correction: [link](https://bit.ly/3GqjI3v)
  - Shor encoding with phase-flip error correction: [link](https://bit.ly/3YXE0IF)

### Quantum Teleportation
- Transmitting the state of 1 qubit using 2 classical bits
- [Link](https://bit.ly/3jPp7Z6)

### Deutsch's Algorithm
- Finding the parity of two bits with one oracle
  - Quirk: [link](https://bit.ly/3GBFeCr)
  - IBM: [link](https://ibm.co/3Cn3qGc)

### Deutsch-Jozsa Algorithm
- Finding the parity of a string of bits
  - Quirk: [link](https://bit.ly/3VL3HJQ)
  - IBM: [link](https://ibm.co/3GH9kEK)

### Bernstein-Vazirani Algorithm
- Finding the value of a bit string `s`, dotted into an input bit string
  - Quirk: [link](https://bit.ly/3vEwlBN)
  - IBM: [link](https://ibm.co/3vDMIOY)

### Grover's Algorithm
- Quantum search / brute force
  - Quirk (4 input qubits with answer `w = 1011`): [link](https://bit.ly/3QizMHO)

### Quantum Fourier Transform
- Calculate the discrete Fourier transform quantumly!

### Phase / Eigenvalue Estimation (circuit on cover of textbook)
- Quantum gates are unitary, so their eigenvalues are of the form `e^(ix)`, where `x` is real and is the phase of the eigenvalue
- Upper part input and output is n-bit eigenvector of matrix U --- eigenstate |v>
- Lower part output is m-bit binary decimal `j` that gives `x = 2pi * j`
  - So we estimate the phase --> eigenvalue with m bits of precision
  - Quirk: [link](https://tinyurl.com/emcnnxfk)
  - Quirk (6 qubits): [link](https://bit.ly/3ikGUqE)

### Finding The Period of a Modular Exponentiation
- Find the (nontrivial) value of `x` such that `a^x mod m = a^0 mod m = 1 mod m`
  - Quirk: (3^x mod 7) [link](https://bit.ly/3ihNhec)
  - Quirk (IQFT): [link](https://bit.ly/3CtXJ9f)

