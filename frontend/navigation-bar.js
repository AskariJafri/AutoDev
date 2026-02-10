import React from 'react';
import './styles.css';

const Navbar = () => {
  const [isOpen, setIsOpen] = React.useState(false);
  const [activeMenu, setActiveMenu] = React.useState(null);

  return (
    <nav>
      <div className="logo">AutoDev</div>
      <ul>
        {menuItems.map((item) => (
          <li key={item.id}>
            <button
              onClick={() => setActiveMenu(item.id)}
              aria-label={item.label}
            >
              {item.icon}
            </button>
            {activeMenu === item.id && (
              <ul className="dropdown">
                {item.subItems.map((subItem) => (
                  <li key={subItem.id}>
                    <a href="#" onClick={() => setActiveMenu(null)}>
                      {subItem.label}
                    </a>
                  </li>
                ))}
              </ul>
            )}
          </li>
        ))}
      </ul>
      <input type="search" placeholder="Search..." />
    </nav>
  );
};

const menuItems = [
  {
    id: 'home',
    label: 'Home',
    icon: '<i class="fas fa-home"></i>',
    subItems: [
      { id: 'about', label: 'About' },
      { id: 'contact', label: 'Contact' },
    ],
  },
  // ...
];

export default Navbar;