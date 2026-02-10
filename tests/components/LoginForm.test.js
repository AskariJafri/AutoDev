import React from 'react';
import { LoginForm } from '../components';
import { render, fireEvent, waitFor } from '@testing-library/react';

describe('LoginForm', () => {
  it('renders email and password fields', () => {
    const { getByText, getByPlaceholderValue } = render(<LoginForm />);
    expect(getByText('Email')).toBeInTheDocument();
    expect(getByText('Password')).toBeInTheDocument();
  });

  it('submits form with correct credentials', async () => {
    const { getByPlaceholderValue, getByText } = render(<LoginForm />);
    const emailInput = getByPlaceholderValue('email');
    const passwordInput = getByPlaceholderValue('password');
    fireEvent.change(emailInput, { target: { value: 'test@example.com' } });
    fireEvent.change(passwordInput, { target: { value: 'password123' } });
    const submitButton = getByText('Login');
    await fireEvent.click(submitButton);
    expect(getByText('Login form submitted: test@example.com password123')).toBeInTheDocument();
  });

  it('displays error message on invalid input', async () => {
    const { getByPlaceholderValue, getByText } = render(<LoginForm />);
    const emailInput = getByPlaceholderValue('email');
    fireEvent.change(emailInput, { target: { value: 'invalid' } });
    const submitButton = getByText('Login');
    await fireEvent.click(submitButton);
    expect(getByText('Invalid credentials')).toBeInTheDocument();
  });
});