import React from 'react';
import { render } from '@testing-library/react';
import NavigationMenu from './NavigationMenu';

test('renders navigation menu', () => {
  const { getByText } = render(<NavigationMenu />);
  expect(getByText('Home')).toBeInTheDocument();
});