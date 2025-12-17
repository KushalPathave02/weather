import { useState } from 'react';
import { postQuery } from './services/api';

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await postQuery(message);
      setResponse(res.response);
    } catch (error) {
      setResponse('Error fetching response from backend.');
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center">
      <div className="w-full max-w-2xl p-8 space-y-8">
        <h1 className="text-4xl font-bold text-center">Weather Agent</h1>
        <form onSubmit={handleSubmit} className="flex items-center space-x-4">
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Ask about the weather..."
            className="w-full p-4 bg-gray-800 border border-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="submit"
            disabled={loading}
            className="px-6 py-4 bg-blue-600 rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-500 disabled:cursor-not-allowed"
          >
            {loading ? 'Loading...' : 'Submit'}
          </button>
        </form>
        {response && (
          <div className="p-4 mt-8 bg-gray-800 border border-gray-700 rounded-lg">
            <p className="text-lg">{response}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
