Web VPython 3.2

# Passo do visualizador
passo = 300

# Sistema de lorenz
def lorenz(x, y, z, sigma, rho, beta):
    x_ponto = sigma * (y - x)
    y_ponto = x*(rho - z) - y
    z_ponto = x*y - beta*z
    return x_ponto, y_ponto, z_ponto

# Rk$ para trajetórias
def rk4_lorenz(x0, y0, z0, sigma, rho, beta, tf, dt):
  t = arange(0, tf+dt, dt)
  tsize = len(t)
  
  x, y, z = [], [], []
  for i in range(0, tsize):
      x.append(0)
      y.append(0)
      z.append(0)

  x[0] = x0
  y[0] = y0
  z[0] = z0

  for i in range(tsize-1):
    k1, l1, m1 = lorenz( x[i], y[i], z[i], sigma, rho, beta)

    k2, l2, m2 = lorenz( x[i] + 0.5*k1*dt, y[i] + 0.5*l1*dt, z[i] + 0.5*m1*dt, sigma, rho, beta)

    k3, l3, m3 = lorenz( x[i] + 0.5*k2*dt, y[i] + 0.5*l2*dt, z[i] + 0.5*m2*dt, sigma, rho, beta)

    k4, l4, m4 = lorenz( x[i] + k3*dt, y[i] + l3*dt, z[i] + m3*dt, sigma, rho, beta)

    x[i+1] = x[i] + dt*(1/6)*(k1 + 2*k2 + 2*k3 + k4)
    y[i+1] = y[i] + dt*(1/6)*(l1 + 2*l2 + 2*l3 + l4)
    z[i+1] = z[i] + dt*(1/6)*(m1 + 2*m2 + 2*m3 + m4)

  return x, y, z, t



# Condições inicias
sigma = 10
beta = 8/3
rho = 28

# Vetor da trajetoria simulada
v = rk4_lorenz(x0=0, y0=1, z0=0, sigma=sigma, rho=rho, beta=beta, tf=100, dt=0.01)

# Curva seguindo os pontos simulados
c = curve(pos=vector(v[0][0],v[1][0],v[2][0]), color=color.red, radius=0.3)

# Função para atualizar no tempo as linhas das trajetórias
for i in range( 1, len(v[3]) ):
    rate(passo)
    c.append( vector( v[0][i],v[1][i],v[2][i] ) )