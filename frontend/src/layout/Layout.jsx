import Navbar from "../components/common/Navbar";
import Footer from "../components/common/Footer";

const Layout = ({ children }) => {
  return (
    <>
      <Navbar />

      <main>
        {children}
      </main>

      <Footer />
    </>
  );
};

export default Layout;