import { useEffect, useMemo, useState } from "react";
import { fetchProducts } from "../api/products";
import Product from "../components/Product/Product";
import { useSearchParams } from "react-router-dom";

const ProductsPage = () => {
  const [data, setData] = useState([]);
  const [params, setParams] = useSearchParams();

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetchProducts();
      setData(res);
    };
    fetchData();
  }, []);

  const handleChange = ({ target: { value } }) => {
    if (!value) return setParams({});
    params.set("search", value);
    setParams(params);
  };

  const searchValue = params.get("search") ?? "";

  const filteredData = useMemo(
    () =>
      data.filter((el) =>
        el.title.toLowerCase().includes(searchValue.toLowerCase())
      ),
    [data, searchValue]
  );

  return (
    <div>
      <div>
        <label htmlFor="search">Search by title</label>
        <br />
        <input
          type="text"
          placeholder="title"
          value={searchValue}
          onChange={handleChange}
        />
      </div>
      {filteredData.length > 0 &&
        filteredData.map((el) => <Product product={el} key={el.id} />)}
    </div>
  );
};

export default ProductsPage;