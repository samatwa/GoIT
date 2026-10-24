import { Route, Routes } from "react-router-dom";
import Navigation from "./components/Navigation/Navigation";
import { lazy, Suspense } from "react";
import TodosPage from "./pages/TodosPage";

const HomePage = lazy(() => import("./pages/HomePage.jsx"));
const ArticlesPage = lazy(() => import("./pages/ArticlesPage"));
const ProductsPage = lazy(() => import("./pages/ProductsPage"));
const ProductDetailsPage = lazy(() => import("./pages/ProductDetailsPage"));
const Category = lazy(() => import("./components/Category/Category"));
const Images = lazy(() => import("./components/Images/Images"));

const App = () => {
  return (
    <div>
      <Navigation />

      <Suspense fallback={<p>Loading component..</p>}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/articles" element={<ArticlesPage />} />
          <Route path="/products" element={<ProductsPage />} />
          <Route path="/products/:id" element={<ProductDetailsPage />}>
            <Route path="category" element={<Category />} />
            <Route path="images" element={<Images />} />
          </Route>
          <Route path="/todos" element={<TodosPage />} />
          <Route path="*" element={<div>404 page</div>} />
        </Routes>
      </Suspense>
    </div>
  );
};

export default App;
