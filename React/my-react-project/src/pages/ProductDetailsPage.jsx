import {
  Link,
  Outlet,
  useLocation,
  useNavigate,
  useParams,
} from "react-router-dom";
import { fetchSingleProduct } from "../api/products";
import { Suspense, useEffect, useRef, useState } from "react";

const ProductDetailsPage = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const location = useLocation();
  const navigate = useNavigate();

  const backLink = useRef(location.state ?? "/products");

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetchSingleProduct(id);
      setProduct(res);
    };
    fetchData();
  }, [id]);

  const handleBack = () => {
    const res = prompt("Are your sure?");
    if (res !== null) {
      navigate(backLink.current);
    }
  };
  return (
    <div>
      <button onClick={handleBack}>Back</button>
      {/* <Link to={location.state}>{`<`} Back</Link> */}
      {product && (
        <>
          <div>
            <h2>{product.id}</h2>
            <h2>{product.title}</h2>
            <p>{product.description}</p>
            <h1>{product.price}</h1>
          </div>
          <ul>
            <li>
              <Link to="category">Category</Link>
            </li>
            <li>
              <Link to="images">Images</Link>
            </li>
          </ul>
          <Suspense fallback={<p>Loading child component..</p>}>
            <Outlet />
          </Suspense>
        </>
      )}
    </div>
  );
};

export default ProductDetailsPage;