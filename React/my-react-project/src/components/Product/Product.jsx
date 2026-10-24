import { Link, useLocation } from "react-router-dom";

const Product = ({ product }) => {
  const location = useLocation();
  // navigate(location.state, { state: location })
  return (
    <div>
      <h2>{product.title}</h2>
      <p>{product.description}</p>
      <p>{product.price}</p>
      <Link to={`${product.id}`} state={location}>
        Details
      </Link>
    </div>
  );
};

export default Product;