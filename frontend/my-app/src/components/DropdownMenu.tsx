import React, { useState, useRef } from "react";

type DropdownMenuProps = {
  matchId: string;
};

const DropdownMenu: React.FC<DropdownMenuProps> = ({ matchId }) => {
  const [isOpen, setIsOpen] = useState(false); // Track dropdown visibility
  const dropdownRef = useRef<HTMLDivElement>(null);

  const toggleMenu = () => {
    setIsOpen((prev) => !prev); // Toggle visibility
  };

  const handleClickOutside = (event: MouseEvent) => {
    if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
      setIsOpen(false); // Close the menu if clicked outside
    }
  };

  React.useEffect(() => {
    document.addEventListener("click", handleClickOutside);
    return () => {
      document.removeEventListener("click", handleClickOutside);
    };
  }, []);

  return (
    <div className="relative" ref={dropdownRef}>
      {/* Button to toggle dropdown */}
      <button
        onClick={toggleMenu}
        className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
      >
        Options
      </button>

      {/* Dropdown menu */}
      {isOpen && (
        <div
          className="absolute mt-2 w-48 bg-white border rounded shadow-lg z-50"
        >
          <a
            href={`/match/${matchId}`}
            className="block px-4 py-2 hover:bg-gray-100"
          >
            View Stats
          </a>
          <button className="block px-4 py-2 hover:bg-gray-100 text-left w-full">
            Bookmark Match
          </button>
        </div>
      )}
    </div>
  );
};

export default DropdownMenu;

