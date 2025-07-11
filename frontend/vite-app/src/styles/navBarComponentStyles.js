export const navBarComponentStyles = {
    navBarContainer : 'bg-white shadow-md',
    navLabel : 'container mx-auto px-4 py-3 flex items-center justify-end',
    navLinkList : 'flex space-x-1 gap-5',
    navLink : ({ isActive }) => `px-4 py-2 rounded-md text-sm font-medium transition-colors duration-700' ${
        isActive ? 'bg-blue-100 text-blue-700' 
        : 'text-gray-600 hover:bg-gray-100 hover:text-gray-900'
    }`
}
