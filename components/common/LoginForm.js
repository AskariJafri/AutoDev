import React from 'react';
import { Form, Field, SubmitButton } from '../components';

const LoginForm = () => {
  const [email, setEmail] = React.useState('');
  const [password, setPassword] = React.useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      // TO DO: Implement API call to login user
      console.log('Login form submitted:', email, password);
    } catch (error) {
      // Show error message and report error to monitoring
      showErrorMessage('Invalid credentials');
      reportErrorToMonitoring(error);
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Field label="Email" type="email" value={email} onChange={(event) => setEmail(event.target.value)} />
      <Field label="Password" type="password" value={password} onChange={(event) => setPassword(event.target.value)} />
      <SubmitButton type="submit">Login</SubmitButton>
    </Form>
  );
};

export default LoginForm;