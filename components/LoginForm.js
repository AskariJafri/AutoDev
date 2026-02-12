<form role="form" aria-label="Login Form">
  <TextField
    label="Email"
    type="email"
    register={register('email')}
    error={errors.email}
    aria-label="Email address"
  />
  <TextField
    label="Password"
    type="password"
    register={register('password')}
    error={errors.password}
    aria-label="Password"
  />
  <Button type="submit">Login</Button>
</form>